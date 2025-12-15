from collections import Counter

def top_ips(logs, n=3):
    """
    Returns top n IPs by request count.
    """
    ips = [log['ip'] for log in logs]
    counter = Counter(ips)
    return counter.most_common(n)

def status_summary(logs):
    """
    Returns a count of each HTTP status code.
    """
    statuses = [log['status'] for log in logs]
    counter = Counter(statuses)
    return dict(counter)

def detect_errors(logs):
    """
    Returns logs with status codes 4xx or 5xx.
    """
    errors = [log for log in logs if log['status'].startswith(('4','5'))]
    return errors
