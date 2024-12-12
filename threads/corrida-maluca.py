import threading
import random
import time

# Configurações da corrida
DISTANCIA = 80
CORREDORES = 5

def corrida(nome, resultado):
    posicao = 0
    while posicao < DISTANCIA:
        posicao += 1
        time.sleep(random.random() * 0.5)
        print(f"{nome} | {'*' * posicao}{(DISTANCIA - posicao)*'_'}|")
    resultado.append(nome)

threads = []
resultado = []

print("Iniciando a corrida!\n")

for i in range(CORREDORES):
    nome = f"Corredor {i}"
    t = threading.Thread(target=corrida, args=(nome, resultado))
    threads.append(t)
    t.start()



for t in threads:
    t.join()
    
print("\nA corrida terminou!")
print(f"Pódiu:{resultado}")


    
