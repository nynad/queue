# for queue terminology: when you add: enqueue, removing is dequeue. you need max value
# adding more than the max is called overflow
# queues follow a first in, first out rule 
# trying to remove/shift objects that aren't there is an underflow 
'''

class Queue: 
    def __init__(self,max):
        self.queue=[None]*max 
        self.front=0
        self.rear=0 
        self.max=max 
        self.avaliable=max 