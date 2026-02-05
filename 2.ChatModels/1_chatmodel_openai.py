from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
# ... (imports and setup)
model = ChatOpenAI(model="gpt-4o")
result = model.invoke("Hello") 
# The script stops here. It got the result, but didn't show it!

# THIS LINE IS VITAL - without it, you see nothing!
print(result.content)