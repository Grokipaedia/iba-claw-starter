# iba-claw-starter

**IBA-Governed version of claw-code**

Combines the popular claw-code harness (from the Anthropic Claude Code leak) with **GRK Intent-Bound Authorization**.

While everyone rushes to add more power to claw-code, this adds the critical missing layer: every agent action must match a cryptographically signed human intent.

## Why this matters
The Anthropic leak proved that internal guardrails ("Undercover Mode") fail when the system itself is exposed.  
IBA enforces safety at the architectural level — before any tool call, memory write, or git action.

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-claw-starter.git
cd iba-claw-starter
pip install -r requirements.txt
python run_governed_claw.py
