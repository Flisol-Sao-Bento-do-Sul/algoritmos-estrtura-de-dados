import unittest

from algoritmos_estrutura_de_dados.src.deque import Deque

class TestDequeMethods(unittest.TestCase):

    def testEnqueueFront(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        s.enqueue_front(-10)
        self.assertEquals(-10, s.first())

    def testEnqueueBack(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        s.enqueue_back(1000)
        self.assertEquals(1000, s.last())
 
    def testDequeueFront(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        element = s.dequeue_front()
        print(element)
        self.assertEquals(10, element)
 
    def testDequeueFrontEmpty(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        s.clear()
        element = s.dequeue_front()
        print(element)
        self.assertEquals(None, element)
 
    def testDequeueBack(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        element = s.dequeue_back()
        print(element)
        self.assertEquals(80, element)
 
    def testPopBackEmpty(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        s.clear()
        element = s.dequeue_back()
        print(element)
        self.assertEquals(None, element)
 
    def testSize(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        self.assertEquals(8, s.size())
 
    def testFirst(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        self.assertEquals(10, s.first())
 
    def testFirstNone(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        s.clear()
        self.assertEquals(None, s.first())
 
    def testLast(self):
        s = Deque()
        s.enqueue_back(10)
        s.enqueue_back(20)
        s.enqueue_back(30)
        s.enqueue_back(40)
        s.enqueue_back(50)
        s.enqueue_back(60)
        s.enqueue_back(70)
        s.enqueue_back(80)
        self.assertEquals(80, s.last())
 

if __name__ == '__main__':
    unittest.main()
