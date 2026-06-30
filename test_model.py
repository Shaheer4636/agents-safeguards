import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# =====================
# Client Setup
# =====================
client = AzureOpenAI(
    api_key=os.getenv("AZURE_FOUNDRY_API_KEY"),
    azure_endpoint=os.getenv("AZURE_FOUNDRY_ENDPOINT"),
    api_version=os.getenv("AZURE_FOUNDRY_API_VERSION"),
    # Responses API ke liye
)

# =====================
# Simple Test
# =====================
print("🔍 Testing GPT-5.4-mini connection...")

try:
    response = client.responses.create(
        model=os.getenv("AZURE_FOUNDRY_MODEL"),
        input="Say hello and tell me your model name.",
    )
    print("✅ Connection successful!")
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("Trying chat completions instead")
    
    # Fallback to chat completions
    response = client.chat.completions.create(
        model=os.getenv("AZURE_FOUNDRY_MODEL"),
        messages=[
            {"role": "user", "content": "Say hello!"}
        ]
    )
    print(f"✅ Chat completions works!")
    print(f"Response: {response.choices[0].message.content}")
