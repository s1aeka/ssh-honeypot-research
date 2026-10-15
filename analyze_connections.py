import re
from collections import Counter

PATTERN = re.compile(r"user=(\S+) password=(\S+)")

def connection_info(line):
    match = PATTERN.search(line)
    if match is None:
        return None
    user, password = match.groups()
    return user, password


users = Counter()
passwords = Counter()

with open("connections.log") as f:
    for line in f:
        result = connection_info(line)
        if result is None:
            continue
        user, password = result
        users[user] += 1
        passwords[password] += 1

print("Top logins:", users.most_common(3))
print("Top passwords:", passwords.most_common(3))                                         