"""
Azure AI Foundry — Endpoint Debug Script
Har possible combination try karta hai
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_FOUNDRY_API_KEY", "")
MODEL   = os.getenv("AZURE_FOUNDRY_MODEL", "gpt-5.4-mini")

if not API_KEY:
    print("❌ API_KEY missing in .env!")
    print("   AZURE_FOUNDRY_API_KEY=your_key_here   .env mein daalo")
    exit(1)

# ─── All endpoint combinations to try ────────────────────────────────────────

COMBINATIONS = [

    # ── 1. Azure AI Foundry — Responses API ──────────────────────────────────
    {
        "name": "Azure Foundry → Responses API (v1)",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/v1/responses",
        "headers": {
            "api-key": API_KEY,
            "Content-Type": "application/json",
        },
        "body": {
            "model": MODEL,
            "input": "Say hello!",
        },
    },

    # ── 2. Azure AI Foundry — Chat Completions (v1) ───────────────────────────
    {
        "name": "Azure Foundry → Chat Completions (v1)",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/v1/chat/completions",
        "headers": {
            "api-key": API_KEY,
            "Content-Type": "application/json",
        },
        "body": {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Say hello!"}],
        },
    },

    # ── 3. Azure AI Foundry — Chat Completions with api-version ──────────────
    {
        "name": "Azure Foundry → Chat Completions (api-version=2026-03-17)",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/deployments/gpt-5.4-mini/chat/completions?api-version=2026-03-17",
        "headers": {
            "api-key": API_KEY,
            "Content-Type": "application/json",
        },
        "body": {
            "messages": [{"role": "user", "content": "Say hello!"}],
        },
    },

    # ── 4. Azure OpenAI standard format ───────────────────────────────────────
    {
        "name": "Azure OpenAI → Standard deployments format",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/deployments/gpt-5.4-mini/chat/completions?api-version=2024-12-01-preview",
        "headers": {
            "api-key": API_KEY,
            "Content-Type": "application/json",
        },
        "body": {
            "messages": [{"role": "user", "content": "Say hello!"}],
        },
    },

    # ── 5. Bearer token instead of api-key ───────────────────────────────────
    {
        "name": "Bearer Token → Chat Completions",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/v1/chat/completions",
        "headers": {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        "body": {
            "model": MODEL,
            "messages": [{"role": "user", "content": "Say hello!"}],
        },
    },

    # ── 6. Models list — check what's available ───────────────────────────────
    {
        "name": "List available models",
        "url" : "https://aimodelsshaheer.services.ai.azure.com/openai/v1/models",
        "headers": {
            "api-key": API_KEY,
            "Content-Type": "application/json",
        },
        "body": None,   # GET request
    },
]

# ─── Runner ───────────────────────────────────────────────────────────────────

print("=" * 65)
print("  Azure AI Foundry — Endpoint Debugger")
print("=" * 65)
print(f"  Model : {MODEL}")
print(f"  Key   : {API_KEY[:8]}{'*' * (len(API_KEY)-8) if len(API_KEY) > 8 else '***'}")
print("=" * 65)

working = []

for i, combo in enumerate(COMBINATIONS, 1):
    print(f"\n[{i}/{len(COMBINATIONS)}] {combo['name']}")
    print(f"    URL: {combo['url']}")

    try:
        if combo["body"] is None:
            # GET request (models list)
            r = requests.get(
                combo["url"],
                headers=combo["headers"],
                timeout=15,
            )
        else:
            r = requests.post(
                combo["url"],
                headers=combo["headers"],
                json=combo["body"],
                timeout=30,
            )

        print(f"    Status: {r.status_code}")

        if r.status_code == 200:
            data = r.json()
            print("    ✅ SUCCESS!")

            # Response content print karo
            if "output_text" in data:
                print(f"    Reply: {data['output_text'][:100]}")
            elif "choices" in data:
                msg = data["choices"][0].get("message", {})
                print(f"    Reply: {msg.get('content','')[:100]}")
            elif "data" in data:
                # Models list
                models = [m.get("id","?") for m in data["data"][:10]]
                print(f"    Models: {models}")
            else:
                print(f"    Data: {json.dumps(data)[:200]}")

            working.append(combo["name"])

        else:
            # Error details
            try:
                err = r.json()
                msg = err.get("error", {}).get("message", r.text[:150])
            except Exception:
                msg = r.text[:150]
            print(f"    ❌ Error: {msg}")

    except requests.exceptions.Timeout:
        print("    ⏱️  Timeout (>15s)")
    except requests.exceptions.ConnectionError as e:
        print(f"    🔌 Connection error: {str(e)[:80]}")
    except Exception as e:
        print(f"    💥 Unexpected: {str(e)[:80]}")

# ─── Summary ──────────────────────────────────────────────────────────────────

print("\n" + "=" * 65)
print("  SUMMARY")
print("=" * 65)

if working:
    print(f"\n✅ Working combinations ({len(working)}):")
    for w in working:
        print(f"   → {w}")
    print("\n👆 Use the first working one in your test_model.py")
else:
    print("\n❌ Nothing worked. Possible issues:")
    print("   1. API key galat hai — MS Foundry se dobara copy karo")
    print("   2. Model name galat hai — 'gpt-5.4-mini' exact hai?")
    print("   3. Endpoint URL galat hai")
    print("   4. Subscription expired / quota issue")
    print("\n📋 Try karo MS Foundry portal pe:")
    print("   Project Settings → Endpoints → apna exact URL copy karo")
    print("   Keys → Primary key copy karo")

print("=" * 65)
