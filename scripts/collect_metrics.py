
import csv
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = ROOT / "metrics" / "events.csv"
JSON_FILE = ROOT / "metrics" / "dora-metrics.json"

def parse_time(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

events = []

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        row["parsed_time"] = parse_time(row["timestamp"])
        events.append(row)

events.sort(key=lambda e: e["parsed_time"])

changes = defaultdict(list)
for event in events:
    changes[event["change_id"]].append(event)

lead_times = []
recovery_times = []
failed_changes = set()
deployment_count = 0

for change_id, items in changes.items():
    starts = [e["parsed_time"] for e in items
              if e["event_type"] == "change_started"]
    deployments = [e["parsed_time"] for e in items
                   if e["event_type"] == "deployment"]
    failures = [e["parsed_time"] for e in items
                if e["event_type"] == "failure"]
    recoveries = [e["parsed_time"] for e in items
                  if e["event_type"] == "recovery"]

    deployment_count += len(deployments)

    if starts and deployments:
        start = min(starts)
        later_deployments = [t for t in deployments if t >= start]
        if later_deployments:
            lead_times.append(
                (min(later_deployments) - start).total_seconds() / 3600
            )

    if deployments and failures:
        failed_changes.add(change_id)

    for failure in failures:
        later_recoveries = [t for t in recoveries if t >= failure]
        if later_recoveries:
            recovery_times.append(
                (min(later_recoveries) - failure).total_seconds() / 3600
            )

now = datetime.now(timezone.utc)
week_ago = now - timedelta(days=7)

recent_deployments = sum(
    1 for e in events
    if e["event_type"] == "deployment"
    and week_ago <= e["parsed_time"] <= now
)

metrics = {
    "generated_at": now.isoformat(),
    "source": "metrics/events.csv",
    "lead_time_for_changes_hours": (
        round(sum(lead_times) / len(lead_times), 2)
        if lead_times else None
    ),
    "deployment_frequency_last_7_days": recent_deployments,
    "mttr_hours": (
        round(sum(recovery_times) / len(recovery_times), 2)
        if recovery_times else None
    ),
    "change_failure_rate_percent": (
        round(len(failed_changes) / deployment_count * 100, 2)
        if deployment_count else None
    ),
    "deployment_count_total": deployment_count,
    "failed_change_count": len(failed_changes),
    "notes": (
        "Metrics are calculated from the events recorded in the CSV. "
        "Deployment frequency counts deployments in the last 7 days. "
        "Change failure rate uses changes with a recorded failure "
        "divided by the total number of deployments."
    )
}

JSON_FILE.parent.mkdir(parents=True, exist_ok=True)
with JSON_FILE.open("w", encoding="utf-8") as f:
    json.dump(metrics, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(json.dumps(metrics, ensure_ascii=False, indent=2))
