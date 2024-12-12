import asyncio
import aioconsole


async def msg_blink(texto):
	try:
		while True:
			print("\r" + " " * len(texto), end="")
			await asyncio.sleep(0.5)
			print(f"\r{texto}", end="")
			await asyncio.sleep(0.5)

	except asyncio.CancelledError:
		print("Fim de pisca")
   
async def main():
	task = asyncio.create_task(msg_blink("loading…"))

	await aioconsole.ainput("Pressione ENTER para sair \n")
	task.cancel()
	
	await task 

asyncio.run(main())
