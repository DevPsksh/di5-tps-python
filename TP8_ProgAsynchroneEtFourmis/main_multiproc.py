from multiprocessing import Process

def calcul_long(name):
    n = 1E7
    while n>0:
        if n % 100 == 0:
            print("Hello from thread " + str(name))
        n -= 1

if __name__ == '__main__':
    processes = [Process(target=calcul_long, args=('process'+str(i),)) for i in range(10)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
