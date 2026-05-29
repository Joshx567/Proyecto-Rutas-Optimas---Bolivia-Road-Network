import time

def medir_tiempo(func):

    inicio = time.time()

    func()

    fin = time.time()

    print("Tiempo:", fin - inicio)