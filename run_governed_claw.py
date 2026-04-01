
**File 3: `run_governed_claw.py`**
```python
# run_governed_claw.py - Simple IBA wrapper for claw-code style agents
import json
from datetime import datetime

def validate_iba(cert_json: str, action: str) -> bool:
    try:
        cert = json.loads(cert_json)
        if datetime.fromisoformat(cert.get("valid_until", "2020-01-01")) < datetime.now():
            print("🚫 IBA BLOCKED: Certificate expired")
            return False
        if action not in cert.get("scope", []):
            print(f"🚫 IBA BLOCKED: '{action}' outside signed intent scope")
            return False
        print(f"✅ IBA ALLOWED: {action} (signed by {cert['iss']})")
        return True
    except Exception as e:
        print(f"🚫 IBA ERROR: Invalid certificate - {e}")
        return False

# Example signed intent certificate (same style as grk-html-2 demo)
DEMO_CERT = '''
{"iss": "human-operator", "intent_id": "iba-claw-001", 
 "scope": ["tool_call", "memory_write", "query", "undercover_commit", "summarize"], 
 "valid_until": "2027-12-31", "sig": "ES256:demo-signature"}
'''

def governed_action(action_name: str):
    """Wrapper: Only run action if IBA validates it"""
    if validate_iba(DEMO_CERT, action_name):
        print(f"🔧 Executing governed action: {action_name}")
        # Here you would call real claw-code functions (tool calling, memory, etc.)
        # Example: claw_code.run_tool(action_name)
    else:
        print("⛔ Action aborted by Governing Layer.")

if __name__ == "__main__":
    print("🚀 iba-claw-starter started — IBA Governing Layer active\n")
    governed_action("query")
    governed_action("memory_write")
    governed_action("leak_internal_code")  # This gets blocked
    governed_action("undercover_commit")
