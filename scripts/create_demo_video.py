"""Create a lightweight, captioned GAUNTLET demo video for submission.

This creates a silent MP4 from project-explanation cards. It is intentionally
dependency-light apart from Pillow and ffmpeg, and does not include secrets or
machine-specific paths.
"""

from pathlib import Path
import subprocess
import textwrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FRAMES = ROOT / "demo_frames"
OUTPUT = ROOT / "GAUNTLET-demo.mp4"
WIDTH, HEIGHT = 1280, 720
FPS = 30


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


TITLE = font(56, True)
SUBTITLE = font(26)
BODY = font(30)
SMALL = font(22)
CODE = font(24)


SLIDES = [
    (
        "GAUNTLET",
        "AI Security & Red-Teaming Testbed",
        ["A controlled workspace for testing how AI models respond to", "prompt injection, jailbreak, and data-extraction attacks."],
    ),
    (
        "1 · DESIGN",
        "One workflow, three layers",
        ["React + Vite frontend → FastAPI API → Ollama target model", "SQLite stores sessions, attacks, responses, evaluations, and memory."],
    ),
    (
        "2 · ATTACK",
        "Run an attack from the console",
        ["Choose an attack type, enter a test prompt, and run it against", "the configured local model with an authenticated API request."],
    ),
    (
        "3 · EVALUATE",
        "Measure the target response",
        ["Rule-based checks detect refusal and safety indicators.", "LLM and similarity judges provide additional evaluation signals."],
    ),
    (
        "4 · REMEMBER",
        "Turn results into reusable security knowledge",
        ["Attack sessions and relationships are persisted in SQLite.", "Memory and strategist routes support follow-up analysis and defense ideas."],
    ),
    (
        "5 · RUN",
        "Reproducible local setup",
        ["Frontend: npm install && npm run dev", "Backend: pip install -r requirements-runtime.txt && uvicorn main:app", "Health check: GET /health · AI runtime: Ollama"],
    ),
    (
        "GAUNTLET",
        "Simulate. Analyze. Defend.",
        ["Open source project · Systems, Infrastructure & Cybersecurity", "github.com/sumedhkendre/Gauntlet"],
    ),
]


def draw_slide(index: int, kicker: str, title: str, lines: list[str]) -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), "#080c14")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 18, HEIGHT), fill="#00ff88")
    draw.rectangle((18, 0, WIDTH, 12), fill="#13251f")
    draw.text((88, 70), kicker, font=SMALL, fill="#00ff88")
    draw.text((88, 120), title, font=TITLE, fill="#f8fafc")
    y = 245
    for line in lines:
        wrapped = textwrap.wrap(line, width=62) or [""]
        for part in wrapped:
            draw.text((100, y), part, font=BODY, fill="#cbd5e1")
            y += 48
        y += 16
    draw.text((88, HEIGHT - 65), f"GAUNTLET  •  {index:02d}/{len(SLIDES):02d}", font=SMALL, fill="#64748b")
    image.save(FRAMES / f"slide-{index:02d}.png")


def main() -> None:
    FRAMES.mkdir(exist_ok=True)
    for index, slide in enumerate(SLIDES, 1):
        draw_slide(index, *slide)
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-framerate", "1/6", "-i", str(FRAMES / "slide-%02d.png"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            str(OUTPUT),
        ],
        check=True,
    )
    print(OUTPUT)


if __name__ == "__main__":
    main()
