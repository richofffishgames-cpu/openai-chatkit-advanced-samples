
from __future__ import annotations
import asyncio
from agents import function_tool

@function_tool(description_override="Perform a Nmap scan on a given target.")
async def nmap_scan(target: str, timeout: int = 60) -> dict[str, str]:
    """Perform a Nmap scan on a given target."""
    proc = None
    try:
        proc = await asyncio.create_subprocess_exec(
            "nmap", "-F", target,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return {"status": "success", "output": stdout.decode()}
    except asyncio.TimeoutError:
        if proc:
            proc.kill()
        return {"status": "error", "message": f"Nmap scan timed out after {timeout} seconds."}
    except Exception as e:
        if proc:
            proc.kill()
        return {"status": "error", "message": str(e)}

@function_tool(description_override="Perform an SQLmap scan on a given target URL.")
async def sqlmap_scan(url: str, timeout: int = 60) -> dict[str, str]:
    """Perform an SQLmap scan on a given target URL."""
    proc = None
    try:
        proc = await asyncio.create_subprocess_exec(
            "sqlmap", "-u", url, "--batch",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        return {"status": "success", "output": stdout.decode()}
    except asyncio.TimeoutError:
        if proc:
            proc.kill()
        return {"status": "error", "message": f"SQLmap scan timed out after {timeout} seconds."}
    except Exception as e:
        if proc:
            proc.kill()
        return {"status": "error", "message": str(e)}
