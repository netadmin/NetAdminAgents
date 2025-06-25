from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict
import uuid

app = FastAPI(
    title="MCP Directory Service",
    version="2025.03.26",
    description="A directory service for MCP-compliant agents."
)

# Agent descriptor model per MCP spec
class AgentDescriptor(BaseModel):
    id: str
    name: str
    mcp_endpoint: str
    capabilities: List[str]
    version: str
    status: Optional[str] = "active"
    metadata: Optional[Dict[str, str]] = {}

# In-memory store (replace with DB for production)
AGENT_DB: Dict[str, AgentDescriptor] = {}

@app.post("/mcp/register", response_model=AgentDescriptor)
def register_agent(agent: AgentDescriptor):
    AGENT_DB[agent.id] = agent
    return agent

@app.delete("/mcp/deregister/{agent_id}")
def deregister_agent(agent_id: str):
    if agent_id in AGENT_DB:
        del AGENT_DB[agent_id]
        return {"detail": "Agent deregistered"}
    else:
        raise HTTPException(status_code=404, detail="Agent not found")

@app.get("/mcp/directory", response_model=List[AgentDescriptor])
def list_agents():
    return list(AGENT_DB.values())

@app.get("/mcp/describe", response_model=Dict)
def describe_directory():
    return {
        "id": "directory-service",
        "name": "MCP Directory Service",
        "mcp_endpoint": "/mcp",
        "capabilities": ["register", "deregister", "list", "describe"],
        "version": "2025.03.26",
        "status": "active"
    }