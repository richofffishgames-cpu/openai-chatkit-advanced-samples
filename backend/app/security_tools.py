
from __future__ import annotations
import subprocess
from agents import function_tool

@function_tool(description_override="Perform a Nmap scan on a given target.")
async def nmap_scan(target: str) -> dict[str, str]:
    """Perform a Nmap scan on a given target."""
    try:
        result = subprocess.run(['nmap', '-F', target], capture_output=True, text=True)
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@function_tool(description_override="Perform an SQLmap scan on a given target URL.")
async def sqlmap_scan(url: str) -> dict[str, str]:
    """Perform an SQLmap scan on a given target URL."""
    try:
        result = subprocess.run(['sqlmap', '-u', url, '--batch'], capture_output=True, text=True)
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        return {"status": "error", "message": str(e)}
