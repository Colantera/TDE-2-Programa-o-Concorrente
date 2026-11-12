# Filósofo: uma thread que executa suas atividades.

# Garfo: um recurso compartilhado que só pode ser utilizado por uma thread de cada vez.

# Pensando: a thread não precisa de recursos compartilhados.

# Com fome: a thread quer adquirir os dois recursos.

# Comendo: a thread conseguiu adquirir ambos.

# Condições de Coffman

# Exclusão mútua: um garfo só pode ser usado por um filósofo de cada vez.

# Manter e esperar: o filósofo segura um garfo enquanto aguarda o outro.

# Não preempção: ninguém pode retirar à força o garfo de outro filósofo.

# Espera circular: cada filósofo aguarda um recurso que está com outro, formando um ciclo.


import threading

filosofos = [0, 1, 2, 3, 4]
garfos = [
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
    threading.Lock(),
]


def indentificar_garfos(i):
    garfo_direita = filosofos[i]  # Garfo de mesmo índice
    garfo_esquerda = (filosofos[i] - 1) % 5  # Garfo anterior

    return garfo_direita, garfo_esquerda


# estados
PENSANDO = 0
COM_FOME = 1
COMENDO = 2

estados_filosofos = [PENSANDO, PENSANDO, PENSANDO, PENSANDO, PENSANDO]

ciclos_por_filosofo = 5


def imprimir_estado():
    for filosofo in filosofos:
        if estados_filosofos[filosofo] == PENSANDO:
            print(f"Filósofo {filosofo + 1}: Está pensando.")
        elif estados_filosofos[filosofo] == COM_FOME:
            print(f"Filósofo {filosofo + 1}: Está com fome.")
        elif estados_filosofos[filosofo] == COMENDO:
            print(f"Filósofo {filosofo + 1}: Está comendo.")


# Operação	O que faz
# threading.Lock()	Cria um novo objeto Lock, inicialmente livre
# .acquire()	Tenta adquirir o Lock; normalmente aguarda se estiver ocupado
# .release()	Libera um Lock adquirido

def pegar_garfo(filosofo, garfo):
    