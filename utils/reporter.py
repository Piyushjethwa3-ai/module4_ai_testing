import json
import os

REPORT_FILE = os.path.join("reports", "results.json")

def save_result(test_name, prompt, response, status):
    os.makedirs("reports", exist_ok=True)   # ✅ FIX

    data = {
        "test": test_name,
        "prompt": prompt,
        "response": response,
        "status": status
    }

    if not os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "w") as f:
            json.dump([], f)

    with open(REPORT_FILE, "r+") as f:
        existing = json.load(f)
        existing.append(data)
        f.seek(0)
        json.dump(existing, f, indent=4)