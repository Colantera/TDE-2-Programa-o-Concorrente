
import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def thread_1():
    LOCK_A.acquire()
    print("T1 adquiriu LOCK_A")

    time.sleep(0.05)

    print("T1 aguardando LOCK_B")
    LOCK_B.acquire()

    print("T1 concluido")

    LOCK_B.release()
    LOCK_A.release()


def thread_2():
    LOCK_B.acquire()
    print("T2 adquiriu LOCK_B")

    time.sleep(0.05)

    print("T2 aguardando LOCK_A")
    LOCK_A.acquire()

    print("T2 concluido")

    LOCK_A.release()
    LOCK_B.release()


t1 = threading.Thread(target=thread_1, daemon=True)
t2 = threading.Thread(target=thread_2, daemon=True)

t1.start()
t2.start()

t1.join(timeout=2)
t2.join(timeout=2)

if t1.is_alive() and t2.is_alive():
    print("Deadlock encontrado")
