counts = {}

with open("auth.log") as f:
    for line in f:
        ip = line.split()[-1]
        counts[ip] = counts.get(ip, 0) + 1

for ip, n in counts.items():
    print(ip, n)
    if n >= 2:
        print("ALERT: possible brute force from", ip)
    