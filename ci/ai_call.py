import os, json, requests, sys

# Feature flag
if os.getenv("AI_ENABLED", "false").lower() != "true":
    print("AI disabled")
    sys.exit(0)

OPENAI_KEY = os.getenv("OPENAI_KEY")
if not OPENAI_KEY:
    print("No OpenAI key")
    sys.exit(0)

# Read real k6 output
if not os.path.exists("k6-output.log"):
    print("k6-output.log not found")
    sys.exit(1)

with open("k6-output.log", "r") as f:
    k6_log = f.read()

headers = {
    "Authorization": f"Bearer {OPENAI_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": f"""
You are a performance engineer.
Analyze the following k6 load test output.
Highlight:
- SLA breaches
- Errors
- Latency issues
- Overall verdict (PASS / FAIL)

k6 output:
{k6_log}
"""
        }
    ],
    "max_tokens": 300
}

r = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload,
    timeout=20
)

r.raise_for_status()

with open("ai_response.json", "w") as f:
    json.dump(r.json(), f, indent=2)

print("AI summary generated from real k6 results")

