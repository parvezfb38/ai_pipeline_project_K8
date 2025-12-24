import os, json, requests

key = os.getenv("SPEEDCURVE_KEY")
site = os.getenv("SPEEDCURVE_SITE_ID")
site = 844428
print("DEBUG site =", site)
print("DEBUG key  =", key[:4] + "****")


if not key or not site:
    raise SystemExit("SpeedCurve env missing")

url = "https://api.speedcurve.com/v1/deploys"

payload = {
    "siteId": site,
    "note": "CircleCI trigger"
}

# SpeedCurve uses BASIC AUTH
auth = (key, "")

resp = requests.post(url, auth=auth, json=payload)

with open("speedcurve_response.json", "w") as f:
    json.dump({
        "status": resp.status_code,
        "body": resp.text
    }, f, indent=2)

print("SpeedCurve triggered")
