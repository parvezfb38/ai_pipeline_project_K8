import os, json, requests

key = os.getenv("SPEEDCURVE_KEY")
site = os.getenv("SPEEDCURVE_SITE_ID")

if not key or not site:
    raise SystemExit("SpeedCurve env missing")

url = f"https://api.speedcurve.com/v1/sites/{site}/runs"

headers = {
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

resp = requests.post(url, headers=headers, json={"notes": "CircleCI trigger"})

with open("speedcurve_response.json", "w") as f:
    json.dump({
        "status": resp.status_code,
        "body": resp.text
    }, f, indent=2)

print("SpeedCurve triggered")
