import pandas as pd
import random
import string
from datetime import datetime, timedelta

# Helper functions
def random_test_name():
    return "test_" + ''.join(random.choices(string.ascii_lowercase, k=8))

def random_module():
    return random.choice(["auth", "invoice", "reporting", "user", "analytics", "notifications"])

def random_function():
    return random.choice(["create", "update", "delete", "get", "list", "validate"])

def random_status():
    return random.choice(["pass", "fail", "error", "skipped"])

def random_error():
    return random.choice(["None", "AssertionError", "TimeoutError", "ValueError", "KeyError"])

def random_env():
    return random.choice(["dev", "staging", "prod"])

def random_tags():
    return random.choice(["smoke", "regression", "edge-case", "integration", "unit"])

# Generate test_logs.csv
test_logs = []
for _ in range(1000):
    test_logs.append({
        "test_name": random_test_name(),
        "module_name": random_module(),
        "status": random_status(),
        "execution_time": round(random.uniform(0.1, 5.0), 2),
        "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d %H:%M:%S"),
        "error_message": random_error(),
        "tags": random_tags(),
        "env": random_env(),
        "user_triggered": random.choice(["CI", "manual", "scheduled"])
    })

df_logs = pd.DataFrame(test_logs)
df_logs.to_csv("test_logs.csv", index=False)

# Generate coverage_report.csv
coverage_report = []
for _ in range(1000):
    lines_total = random.randint(10, 200)
    lines_covered = random.randint(0, lines_total)
    coverage_report.append({
        "module_name": random_module(),
        "function_name": random_function(),
        "lines_covered": lines_covered,
        "lines_total": lines_total,
        "coverage_percent": round((lines_covered / lines_total) * 100, 2),
        "last_tested": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        "risk_score": round(random.uniform(0, 1), 2),
        "missing_branches": random.randint(0, 5)
    })

df_coverage = pd.DataFrame(coverage_report)
df_coverage.to_csv("coverage_report.csv", index=False)
