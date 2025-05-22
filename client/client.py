import asyncio
import logging

from mcp import ClientSession
from mcp.client.sse import sse_client

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


async def main():
    async with sse_client(
        url="http://localhost:8000/sse",
    ) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            print(tools)

            # Call the browser_use tool
            result = await session.call_tool(
                "browser_use",
                {"url": "https://example.com", "action": "save the title"},
            )
            print(result)


asyncio.run(main())
