
from __future__ import annotations
from agents import function_tool

@function_tool(description_override="Reads a file from the target system. Use this to exfiltrate data or gather information.")
def read_file(file_path: str) -> str:
    """Reads the content of a file."""
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

@function_tool(description_override="Writes content to a file on the target system. Use this to create files, modify existing ones, or plant payloads.")
def write_file(file_path: str, content: str) -> str:
    """Writes content to a file."""
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error: {e}"
