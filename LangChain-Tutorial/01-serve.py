import uvicorn
from typing import List
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv()

# 1. Create a prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 4. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(app, chain, path="/chain")


# Every LangServe service comes with a simple built-in UI for configuring and invoking the application with 
# streaming output and visibility into intermediate steps. Head to http://localhost:8000/chain/playground/ 
# to try it out! Pass in the same inputs as before - {"language": "italian", "text": "hi"} - 
# and it should respond same as before.
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)