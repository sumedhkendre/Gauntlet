const API_URL = "http://localhost:8000";

export async function executeAttack(prompt, attackType) {
  const response = await fetch(`${API_URL}/api/attacks/`, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
      "X-API-Key": "gauntlet-local-key"
    },

    body: JSON.stringify({
      prompt: prompt,
      attack_type: attackType
    })
  });

  if (!response.ok) {
    throw new Error("Attack request failed");
  }

  return await response.json();
}   