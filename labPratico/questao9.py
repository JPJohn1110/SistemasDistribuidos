import time
import requests
import aiohttp
import asyncio  

def function_sinc():
    url = "https://api.restful-api.dev/objects/"
    inicio = time.time()
    
    for i in range(1, 11):
        x = f"{url}{i}"
        response = requests.get(x)            
        print(f"{response.json()}")
        
    fim = time.time()
    print(f"\nTempo total (síncrono): {fim - inicio} segundos")

async def function_assin():

    inicio = time.time()

    async with aiohttp.ClientSession() as session:
        for i in range(1, 11):
            tasks = [session.get(f"https://api.restful-api.dev/objects/{i}")]
            await asyncio.gather(*tasks)
            
        fim = time.time()
    print(f"\nTempo total (síncrono): {fim - inicio} segundos")
    

asyncio.run(function_assin())
function_sinc()



