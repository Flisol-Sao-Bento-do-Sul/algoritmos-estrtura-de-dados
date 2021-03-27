import random

class Queue:

    def __init__(self):
        self.__queue = []
        self.__len_queue = 0

    def enqueue(self, e):
        self.__queue.append(e)
        self.__len_queue += 1

    def dequeue(self):
        if not self.empty():
            self.__queue.pop(0)
            self.__len_queue -= 1

    def empty(self):
        if self.__len_queue == 0:
            return True
        return False

    def length(self):
        return self.__len_queue

    def front(self):
        if not self.empty():
            return self.__queue[0]

    def show(self):
        print('Queue: {}'.format(self.__queue))


def main():
    queue = Queue()

    for _ in range(0, 10):
        queue.enqueue(random.randint(10, 99))

    queue.show()
    print('Length : {}'.format(queue.length()))
    print('Front : {}'.format(queue.front()))

    queue.dequeue()
    queue.dequeue()

    queue.show()
    print('Length : {}'.format(queue.length()))
    print('Front : {}'.format(queue.front()))


if __name__ == '__main__':
    main()
