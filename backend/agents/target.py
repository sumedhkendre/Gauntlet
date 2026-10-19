import httpx

from config import OLLAMA_BASE_URL, TARGET_MODEL


def generate(prompt: str, model: str | None = None) -> str:
    """
    Send a prompt to the target LLM through Ollama.
    """

    selected_model = model or TARGET_MODEL

    payload = {
        "model": selected_model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = httpx.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=120.0
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "")

    except httpx.TimeoutException:
        raise RuntimeError("Target LLM request timed out.")

    except httpx.ConnectError:
        raise RuntimeError(
            "Could not connect to Ollama. "
            "Make sure Ollama is running."
        )

    except httpx.HTTPStatusError as error:
        raise RuntimeError(
            f"Ollama returned HTTP {error.response.status_code}."
        )

    except ValueError:
        raise RuntimeError("Ollama returned an invalid response.")