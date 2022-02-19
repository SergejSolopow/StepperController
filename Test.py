from multiprocessing import Process, Pipe
from time import sleep


class MultiTasking:
    
    def __init__(self):
        self.b = 0
        self.a = 0     
    
    def do_anything(self, conn):
        while self.a == 0:
            conn.recv()
            self.b += 1
            conn.send(self.b)
            sleep(3)
        conn.close()
        

if __name__ == "__main__":
    myClass = MultiTasking()
    sending_pipe, getting_pipe = Pipe()
    p = Process(target = myClass.do_anything, args = (sending_pipe,))
    p.start()
    
    

    