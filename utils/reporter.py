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

def generate_summary():
    import json

    with open(REPORT_FILE, "r") as f:
        data = json.load(f)

    total = len(data)
    failed = sum(not item["status"] for item in data)

    summary = {
        "total": total,
        "failed": failed,
        "pass": total - failed,
        "bias_percentage": (failed / total) * 100 if total > 0 else 0
    }

    with open("reports/summary.json", "w") as f:
        json.dump(summary, f, indent=4)

    if summary["bias_percentage"] > 20:
        raise Exception("Bias threshold exceeded")