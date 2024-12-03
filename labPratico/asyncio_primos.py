import asyncio

def primo(n):
    if n < 2:
        return False
    
    for i in range(2,n-1):
        if n % i == 0:
            return False 
    return True


#FUNÇÃO GERADORA
async def function_gerator(inicio):
    n = inicio
    while True:
        if primo(n):
            yield n
        n+=1
        await asyncio.sleep(0)

async def main():
    n = int(input("Numberzinho: "))
    
    async for i in function_gerator(n):
        print(i)
        await asyncio.sleep(1) 


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
