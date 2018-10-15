from threading import Thread

class MThread(Thread):

    def __init__(self, name, runnable):
        Thread.__init__(self)
        self.name = name
        self.runnable = runnable

    def run(self):
        self.runnable(self.name)

def calcul_long(name):
    n = 1E7
    while n>0:
        if n % 100 == 0:
            print("Hello from thread " + str(name))
        n -= 1

if __name__ == '__main__':
    thread1 = MThread("thread1", calcul_long)
    thread2 = MThread("thread2", calcul_long)
    thread1.start()
    thread2.start()
