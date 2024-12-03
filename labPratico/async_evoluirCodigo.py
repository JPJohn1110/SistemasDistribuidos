import asyncio

async def task(id, segs):
	#Executa algo que não dependa de você…
	#p.ex: Replicação de DB em server secundário
	print(f"Task{id} Iniciada")
	await asyncio.sleep(segs)
	print(f"Task{id} Concluída finalizada em {segs} segundas")

async def main():
	print('Aplicação Iniciada')
	t1 = asyncio.create_task(task(1,5))
	t2 = asyncio.create_task(task(2,8))
	t3 = asyncio.create_task(task(3,3))

	done, pending = await asyncio.wait(
		{t1, t2,t3}, 
		return_when=asyncio.FIRST_COMPLETED
  	)
	
	for i in done:
		await i

asyncio.run(main())
