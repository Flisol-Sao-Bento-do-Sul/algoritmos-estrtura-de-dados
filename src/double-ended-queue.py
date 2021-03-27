import random

class Deque:

    def __init__(self):
        self.__deque = []
        self.__len = 0

    def enqueue_front(self, element):
        self.__deque.insert(0, element)
        self.__len += 1

    def dequeue_front(self):
        element = None
        if not self.empty():
            element = self.__deque.pop(0)
            self.__len -= 1
        return element

    def enqueue_back(self, element):
        if not self.empty():
            self.__deque.insert(self.size(), element)
        else:
            self.__deque.insert(0, element)
        self.__len += 1

    def dequeue_back(self):
        element = None
        if not self.empty():
            element = self.__deque.pop(self.__len -1)
            self.__len -= 1
        return element

    def empty(self):
        if self.__len == 0:
            return True
        return False

    def size(self):
        return self.__len

    def front(self):
        if not self.empty():
            return self.__deque[0]

    def back(self):
        if not self.empty():
            return self.__deque[-1]

    def show(self):
        print('Deque : {}'.format(self.__deque))


def main():
    deque = Deque()

    for _ in range(0, 5):
        deque.enqueue_front(random.randint(10, 99))
        deque.enqueue_back(random.randint(10, 99))

    deque.show()
    print('Back : {}'.format(deque.back()))
    print('Front : {}'.format(deque.front()))

    deque.dequeue_front()
    deque.dequeue_back()

    deque.show()
    print('Back : {}'.format(deque.back()))
    print('Front : {}'.format(deque.front()))


if __name__ == '__main__':
    main()
