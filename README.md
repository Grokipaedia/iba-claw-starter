# iba-claw-starter

**The first simple IBA-governed starter for claw-code**

Everyone is forking claw-code (the Python rewrite of the leaked Anthropic Claude Code architecture) to add more power.

This repo adds the missing piece: **Intent-Bound Authorization (IBA)** from the GRK Governing Layer.

Every action (tool call, memory write, git commit, etc.) must match a cryptographically signed human intent — exactly what Anthropic failed to enforce.

## Features
- Simple IBA validator (pre-action enforcement)
- Clear "ALLOWED" vs "BLOCKED" examples
- Easy to plug into real claw-code functions

## Quick Start
```bash
git clone https://github.com/Grokipaedia/iba-claw-starter.git
cd iba-claw-starter
pip install -r requirements.txt
python run_governed_claw.py
