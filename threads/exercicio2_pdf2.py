import threading
import time

def ola_mundo(idThread):
	print(f'Olá Mundo! Sou a thread {idThread}')
	print("Até mais")	
	time.sleep(2)


threads = []
for i in range(10):
	t = threading.Thread(target=ola_mundo, args=(i+1,),daemon=True)
	t.start()
	#t.join()
	threads.append(t)
