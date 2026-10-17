from fastmcp import FastMCP

from app import _examples


mcp = FastMCP("My MCP Server")

for server in _examples.__all__:
    mcp.mount(getattr(_examples, server), server)

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
