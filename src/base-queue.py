class BaseQueue:

    def __init__(self):
        self.__queue = []
        self.__length = 0

    def empty(self):
        if self.__length == 0:
            return True
        return False

    def size(self):
        return self.__length

    def first(self):
        if not self.empty():
            return self.__queue[0]
        return None
    
    def last(self):
        if not self.empty():
            return self.__queue[-1]
        return None
    
    def clear(self):
        if not self.empty():
            self.__queue.clear()
            self.__length = 0
    
    def show(self, name = ''):
        print('{}: {}'.format(name, self.__queue))
