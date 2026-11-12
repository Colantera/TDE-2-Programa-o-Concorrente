import threading
import time

contador = 0
semaforo = threading.Semaphore(1) #só uma thread entra por vez

def contar():
    global contador

    for i in range(200000):
        semaforo.acquire() #espera a sua vez

        try:
            valor = contador
            time.sleep(0)
            contador = valor + 1
        finally:
            semaforo.release() # libera para a proxima

for teste in range(3):
    contador = 0
    threads = []

    inicio = time.time()

    for i in range(8):
        t = threading.Thread(target=contar)
        threads.append(t)
        t.start()

    for t in threads: #espera todas terminar
        t.join()

    print("Teste:", teste + 1)
    print("Esperado:", 8 * 200000)
    print("Obtido:", contador)
    print("Tempo:", round(time.time() - inicio, 2), "segundos")
    print()
