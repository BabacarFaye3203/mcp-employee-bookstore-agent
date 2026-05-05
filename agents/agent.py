from fastapi import FastAPI
from pydantic import BaseModel

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage

app = FastAPI()

llm = ChatOllama(model="llama3.2:latest", temperature=0)
agent = None


class QueryRequest(BaseModel):
    query: str


@app.on_event("startup")
async def startup():

    global agent

    mcp_client = MultiServerMCPClient({
        "mcp_server": {
            "transport": "streamable-http",
            "url": "http://localhost:2400/mcp"
        }
    })

    tools = await mcp_client.get_tools()

    print("TOOLS:", [t.name for t in tools])

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""
You are an employee assistant.

RULES:
- Always use tools for employee queries
- Return structured answer
"""
    )


@app.post("/query")
async def query(req: QueryRequest):

    result = await agent.ainvoke({
        "messages": [HumanMessage(content=req.query)]
    })

    return {
        "response": result["messages"][-1].content
    }


@app.get("/")
def home():
    return {"status": "ok"}