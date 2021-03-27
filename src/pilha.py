import random

class Stack: 

    def __init__(self):
        self.__stack = []
        self.__len_stack = 0

    def push(self, e):
        self.__stack.append(e)
        self.__len_stack += 1

    def pop(self):
        if not self.empty():
            self.__stack.pop(self.__len_stack - 1)
            self.__len_stack -= 1

    def top(self):
        if not self.empty():
            return self.__stack[-1]
        return None 

    def empty(self):
        if self.__len_stack == 0:
            return True
        return False

    def length(self):
        return self.__len_stack
    
    def show(self):
        print('Stack: {}'.format(self.__stack))


def main():

    stack = Stack()

    for _ in range(0, 10):
        stack.push(random.randint(10, 99))

    stack.length()
    stack.show()

    stack.pop()
    stack.pop()

    stack.length()
    stack.show()


if __name__ == '__main__':
    main()
