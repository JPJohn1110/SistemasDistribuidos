import asyncio
import random
import aiohttp




async def msg_blink(texto):
	try:
		while True:
			print("\r" + " " * len(texto), end="")
			await asyncio.sleep(0.5)
			print(f"\r{texto}", end="")
			await asyncio.sleep(0.5)

	except asyncio.CancelledError:
		print("\r")
  
  
async def get_ip():
    latencia = random.randint(3,10)
    
    await asyncio.sleep(latencia)
    
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.ipify.org?format=json") as response:
            if response.status == 200:
                data = await response.json()
                return data.get("ip")
            else:
                raise Exception("Erro ao obter o IP")


async def main():
    pisca = asyncio.create_task(msg_blink("loading..."))
    
    try:
        ip = await get_ip()
    finally:
        pisca.cancel()
        try:
            await pisca
        except asyncio.CancelledError:
            print(f"\nSeu endereço IP público é: {ip}")

asyncio.run(main())
