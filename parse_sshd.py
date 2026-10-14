import re
from collections import Counter

PATTERN = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+) port")


def parse_line(line):
    match = PATTERN.search(line)
    if match is None:
        return None
    user, ip = match.groups()
    return user, ip


ips = Counter()
users = Counter()

with open("sshd.log") as f:
    for line in f:
        result = parse_line(line)
        if result is None:
            continue
        user, ip = result
        ips[ip] += 1
        users[user] += 1

print("Top IPs:", ips.most_common(2))
print("Top usernames:", users.most_common(3))