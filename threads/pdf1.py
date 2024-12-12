import time
import threading

def task1():
	print("Task1 Iniciada")
	time.sleep(6)
	print("Task1 Concluída")

def task2():
	print("Task2 Iniciada")
	time.sleep(4)
	print("Task2 Concluída")
def main():
	print('Aplicação Iniciada')
	inicio = time.time()
	t1 = threading.Thread(target=task1)
	t2 = threading.Thread(target=task2)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print(f'Execução Finalizada em {time.time()-inicio}')
main()