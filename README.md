# ssh-honeypot-research

A small SSH honeypot written in Python, plus an analysis of the real attack data it collects.

## Goal
Learn how automated SSH attacks work by recording them: which usernames and
passwords bots try, where they come from, and what they do after "logging in".

## Status
Work in progress. Currently: building a log analyzer and a local honeypot.

## Plan
1. Log analyzer for auth logs (Python)
2. Local SSH honeypot (asyncssh)
3. Deployment on an isolated VPS and data collection
4. Analysis and dashboard
5. Fake shell that records commands (never executes them)

## Safety
The honeypot runs only on an isolated server. Nothing sent by attackers is
ever executed. Published data is aggregated and IP addresses are anonymized.
