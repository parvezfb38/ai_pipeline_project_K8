import os, json, requests, sys

if os.getenv("AI_ENABLED", "false").lower() != "true":
    print("AI disabled")
    sys.exit(0)

OPENAI_KEY = os.getenv("OPENAI_KEY")
if not OPENAI_KEY:
    print("No OpenAI key")
    sys.exit(0)

headers = {
    "Authorization": f"Bearer {OPENAI_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "Summarize k6 load test results from CI pipeline"}
    ]
}

r = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=payload,
    timeout=20
)

with open("ai_response.json", "w") as f:
    json.dump(r.json(), f, indent=2)

print("AI summary generated")
