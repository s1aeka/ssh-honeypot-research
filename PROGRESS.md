# Progress

## Done
- analyze.py: counts failed logins per IP
- parse_sshd.py: parses a real sshd log (regex, Counter): top IPs, top usernames, totals
- server.py: TCP server on localhost that asks for login and password and logs each attempt
- bot.py: test client that imitates a bot
- analyze_connections.py: top logins and passwords from connections.log
- Git workflow: status, add, commit, push; .gitignore for logs

## Now
- Understanding how the server and client talk (accept, recv, sendall)

## Problems
- (none right now)

## Next
- Real SSH honeypot with asyncssh
- Set up WSL (Ubuntu) and practice Linux commands
- Rent an isolated VPS and collect real data