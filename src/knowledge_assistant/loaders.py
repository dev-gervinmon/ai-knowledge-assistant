import asyncio


async def load_document(title: str):
    print(f"Loading {title}")
    await asyncio.sleep(2)
    print(f"Finished {title}")
    return title
