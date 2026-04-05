#!/usr/bin/env python3
"""
Simple test script for the DnD MCP server
"""

import asyncio
import sys
from pathlib import Path

# Add the lab11 directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_dnd_server():
    """Test the DnD MCP server tools."""

    # Path to the server
    server_script = Path(__file__).parent / "mcp_server.py"

    print("Testing DnD MCP Server...")
    print(f"Server: {server_script}")

    # Configure the server parameters
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_script)]
    )

    try:
        async with stdio_client(server_params) as (read_stream, write_stream):
            async with ClientSession(read_stream, write_stream) as session:
                # Initialize
                await session.initialize()
                print("✓ Connection initialized")

                # List tools
                tools = await session.list_tools()
                print(f"✓ Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")

                # Test roll_dice
                print("\nTesting roll_dice...")
                result = await session.call_tool("roll_dice", {"n_dice": 2, "sides": 6, "modifier": 2})
                print(f"Result: {result.content[0].text}")

                # Test get_character_stat
                print("\nTesting get_character_stat...")
                result = await session.call_tool("get_character_stat", {"character": "wizard", "stat": "intelligence"})
                print(f"Result: {result.content[0].text}")

                # Test calculate_damage
                print("\nTesting calculate_damage...")
                result = await session.call_tool("calculate_damage", {"base_damage": 10, "armor_class": 15, "attack_roll": 16})
                print(f"Result: {result.content[0].text}")

                print("\n✓ All tests passed!")

    except Exception as e:
        print(f"✗ Error: {e}")
        return False

    return True

if __name__ == "__main__":
    success = asyncio.run(test_dnd_server())
    sys.exit(0 if success else 1)