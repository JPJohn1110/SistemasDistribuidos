import asyncio
import random

async def task(id, segs):
	print(f"Task{id} Iniciada")
	await asyncio.sleep(segs)
	print(f"Task{id} Concluída finalizada em {segs} segundas")

async def main_primeira():

	t = [asyncio.create_task(task(i, random.randint(3,10))) for i in range(30)]

	done, pending = await asyncio.wait(
		t, 
		return_when=asyncio.FIRST_COMPLETED
	)

	for i in done:
		await i
async def main_todas():

	t = [asyncio.create_task(task(i, random.randint(3,10))) for i in range(30)]

	done, pending = await asyncio.wait(
		t, 
		return_when=asyncio.ALL_COMPLETED
	)

	for i in done:
		await i
asyncio.run(main_todas())
