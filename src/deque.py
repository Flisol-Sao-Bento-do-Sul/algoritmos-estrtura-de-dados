from algoritmos_estrutura_de_dados.src.base.basequeue import BaseQueue

import random

class Deque(BaseQueue):

    def __init__(self):
        BaseQueue.__init__(self)

    def enqueue_front(self, element):
        self.__queue.insert(0, element)
        self.__length += 1

    def dequeue_front(self):
        element = None
        if not self.empty():
            element = self.__queue.pop(0)
            self.__length -= 1
        return element

    def enqueue_back(self, element):
        if not self.empty():
            self.__queue.insert(self.size(), element)
        else:
            self.__queue.insert(0, element)
        self.__length += 1

    def dequeue_back(self):
        element = None
        if not self.empty():
            element = self.__queue.pop(self.__length -1)
            self.__length -= 1
        return element
