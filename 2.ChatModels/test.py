from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

# Load .env
load_dotenv()

# 1. Initialize the Endpoint
# We use 'text-generation' here because ChatHuggingFace will convert our 
# messages into the correct string format for us.
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B", 
    max_new_tokens=512,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    # REMOVED: provider='auto' (This was causing the 410 error)
)

# 2. Wrap in ChatHuggingFace
model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You're a helpful assistant"),
    HumanMessage(content="What happens when an unstoppable force meets an immovable object?"),
]

print("Fetching response from DeepSeek...")

try:
    ai_msg = model.invoke(messages)
    print("\n--- AI Response ---")
    print(ai_msg.content)
except Exception as e:
    print(f"\nFailed to get response: {e}")