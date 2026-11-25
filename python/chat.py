import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["NOVAINK_API_KEY"],
    base_url="https://novaink.ai/v1",
)

resp = client.chat.completions.create(
    model="gpt-5",  # Swap freely: claude-sonnet-4-5-20250929, gemini-2.5-pro, deepseek-r1
    messages=[{"role": "user", "content": "Give me 3 concise tips for clean API design."}],
)
print(resp.choices[0].message.content)
