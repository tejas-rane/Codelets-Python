import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10): #when iterating variable is of no use in logic
            print(threading.current_thread().getName())

x = Messenger(name = 'send ')
y = Messenger(name = 'rcv')
x.start()
y.start()