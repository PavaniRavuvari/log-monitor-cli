from monitor.parser import parse_log
from monitor.analyzer import top_ips, status_summary, detect_errors

if __name__ == "__main__":
    logs = parse_log("sample_logs/access.log")

    print("Parsed Logs:")
    for log in logs:
        print(log)

    print("\nTop IPs:")
    print(top_ips(logs))

    print("\nStatus Summary:")
    print(status_summary(logs))

    print("\nErrors Detected:")
    print(detect_errors(logs))
