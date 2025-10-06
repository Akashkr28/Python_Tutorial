import asyncio
import time

async def brew(name):
    print(f"Brwing {name}...")
    # await asyncio.sleep(2)
    time.sleep(3)  # Simulating a blocking operation
    print(f"{name} is ready!")

async def main():
    await asyncio.gather(
        brew("Adrak Chai"),
        brew("Elaichi Chai"),
        brew("Masala Chai")
    )

asyncio.run(main())