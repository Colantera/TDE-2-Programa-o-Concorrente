
# Filósofo: uma thread que executa suas atividades.

# Garfo: um recurso compartilhado que só pode ser utilizado por uma thread de cada vez.

# Pensando: a thread não precisa de recursos compartilhados.

# Com fome: a thread quer adquirir os dois recursos.

# Comendo: a thread conseguiu adquirir ambos.

import threading
import time

filosofos = [0, 1, 2, 3, 4]
garfos = [
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
]

# Estados
PENSANDO = 0
COM_FOME = 1
COMENDO = 2

estados_filosofos = [PENSANDO, PENSANDO, PENSANDO, PENSANDO, PENSANDO]

ciclos_por_filosofo = 1

tempo_log = 0.5

# Evita misturar as mensagens no console
trava_console = threading.Lock()


def mostrar_log(mensagem):
    with trava_console:
        print(mensagem, flush=True)
        time.sleep(tempo_log)


def identificar_garfos(filosofo):
    garfo_direita = filosofo
    garfo_esquerda = (filosofo - 1) % 5

    return garfo_direita, garfo_esquerda


def imprimir_estado():
    with trava_console:
        print("\nEstados dos filósofos:")

        for filosofo in filosofos:
            if estados_filosofos[filosofo] == PENSANDO:
                print(f"Filósofo {filosofo + 1}: Está pensando.")
            elif estados_filosofos[filosofo] == COM_FOME:
                print(f"Filósofo {filosofo + 1}: Está com fome.")
            elif estados_filosofos[filosofo] == COMENDO:
                print(f"Filósofo {filosofo + 1}: Está comendo.")
        print("\n")


def pegar_garfo(filosofo, garfo):
    mostrar_log(f"Filósofo {filosofo + 1} tentando pegar o garfo {garfo}.")

    garfos[garfo].acquire()

    mostrar_log(f"Filósofo {filosofo + 1} pegou o garfo {garfo}.")


def soltar_garfo(filosofo, garfo):
    garfos[garfo].release()
    mostrar_log(f"Filósofo {filosofo + 1} soltou o garfo {garfo}.")


def executar_filosofo(filosofo):
    direita, esquerda = identificar_garfos(filosofo)

    for ciclo in range(ciclos_por_filosofo):
        estados_filosofos[filosofo] = PENSANDO
        mostrar_log(f"Filósofo {filosofo + 1} está pensando.")
        time.sleep(1)

        estados_filosofos[filosofo] = COM_FOME
        mostrar_log(f"Filósofo {filosofo + 1} está com fome.")

        # O último filósofo pega primeiro o garfo esquerdo
        if filosofo == 4:
            pegar_garfo(filosofo, esquerda)
            pegar_garfo(filosofo, direita)

        # Os outros pegam primeiro o garfo direito
        else:
            pegar_garfo(filosofo, direita)
            pegar_garfo(filosofo, esquerda)

        estados_filosofos[filosofo] = COMENDO
        mostrar_log(f"Filósofo {filosofo + 1} está comendo.")
        time.sleep(1)

        soltar_garfo(filosofo, esquerda)
        soltar_garfo(filosofo, direita)

        estados_filosofos[filosofo] = PENSANDO
        mostrar_log(f"Filósofo {filosofo + 1} terminou de comer.")



# Criando as threads
threads = []

for filosofo in filosofos:
    thread = threading.Thread(target=executar_filosofo, args=(filosofo,))
    threads.append(thread)
    thread.start()

for i in range(3):
    time.sleep(7)
    imprimir_estado()

# Aguarda todos os filósofos terminarem seus ciclos
for thread in threads:
    thread.join()

imprimir_estado()
print("\nTodos os filósofos terminaram sem deadlock!")
