
import threading

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def thread_corrigida(nome):
    LOCK_A.acquire()
    print(f"{nome} adquiriu LOCK_A")

    LOCK_B.acquire()
    print(f"{nome} adquiriu LOCK_B")

    print(f"{nome} concluido")

    LOCK_B.release()
    LOCK_A.release()


t1 = threading.Thread(target=thread_corrigida, args=("T1",))
t2 = threading.Thread(target=thread_corrigida, args=("T2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Execução finalizada, sem deadlock")
