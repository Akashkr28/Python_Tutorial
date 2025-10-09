import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"{data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        encrypted = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"Encrypted data: {encrypted}")

if __name__ == "__main__":
    asyncio.run(main())