
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

ciclos_por_filosofo = 5


tempo_log = 0.5


tempo_deadlock = 3

# Evita misturar as mensagens no console
trava_console = threading.Lock()

# Faz todos pegarem um garfo antes de continuar
barreira = threading.Barrier(5)


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

        # Pega primeiro o garfo direito
        pegar_garfo(filosofo, direita)

        # Todos esperam aqui com um garfo
        barreira.wait()

        # Tenta pegar o segundo garfo
        pegar_garfo(filosofo, esquerda)

        estados_filosofos[filosofo] = COMENDO
        mostrar_log(f"Filósofo {filosofo + 1} está comendo.")
        time.sleep(1)

        soltar_garfo(filosofo, esquerda)
        soltar_garfo(filosofo, direita)

        estados_filosofos[filosofo] = PENSANDO
        mostrar_log(f"Filósofo {filosofo + 1} terminou de comer.")

        imprimir_estado()


# Criando as threads
threads = []

for filosofo in filosofos:
    thread = threading.Thread(target=executar_filosofo, args=(filosofo,), daemon=True)
    threads.append(thread)
    thread.start()


# Aguarda as tentativas de pegar os garfos
# O tempo maior permite acompanhar a execução
for thread in threads:
    thread.join(timeout=tempo_deadlock)

if any(thread.is_alive() for thread in threads):
    print("             DEADLOCK DETECTADO!")

    imprimir_estado()

    print("\nTodos os filósofos pegaram um garfo.")
    print("Cada filósofo está esperando o segundo garfo.")
    print("Nenhum consegue comer ou liberar seu garfo.")

else:
    print("\nTodos terminaram.")
