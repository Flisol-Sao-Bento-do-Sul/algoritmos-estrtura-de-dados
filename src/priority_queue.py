'''
    Implementação da Priority queue com a Lsita Ordenada
'''

class Person:

    def __init__(self, name, prior):
        self.__name = name
        self.__prior = prior

    def getName(self):
        return self.__name

    def getPrior(self):
        return self.__prior

class PriorityQueue:

    def __init__(self):
        self.__pq = [] # priority queue
        self.__len = 0 # length of priority queue

    #insere decresentemente pela prioridade
    def push(self, person):

        if self.empty():
            self.__pq.append(person)
        else:

            flag_push = False
            # procura-se onde inserir para manter a fila ordenada
            for i in range(self.__len):
                if (self.__pq[i].getPrior() < person.getPrior()):
                    self.__pq.insert(i, person)
                    flag_push = True
                    break
            
            if not flag_push:
                # se entrou aqui é pq tem inserir ao final
                self.__pq.insert(self.__len, person)
        
        self.__len += 1

    def pop(self):
        if not self.empty():
            self.__pq.pop(0)
            self.__len -= 1

    def empty(self):
        if self.__len == 0:
            return True
        return False

    def show(self):
        for p in self.__pq:
            print('Nome: {}'.format(p.getName()))
            print('Prioridade: {}'.format(p.getPrior()))
            print('')


def main():


    # criando os objetos Person
    person1 = Person('José', 28)
    person2 = Person('Maria', 4)
    person3 = Person('Pedro', 38)
    person4 = Person('João', 50)

    #criando a fila de prioridades e inderindo elementos
    pq = PriorityQueue()
    pq.push(person1)
    pq.push(person2)
    pq.push(person3)
    pq.push(person4)

    print('Exibindo após as inserções: \n')
    pq.show() # João, José, Pedro, Maria

    #removendo elementos
    pq.pop()
    pq.pop()

    print('Exibindo após as remoções: \n')
    pq.show() # José, Maria


if __name__ == "__main__":
    main()
