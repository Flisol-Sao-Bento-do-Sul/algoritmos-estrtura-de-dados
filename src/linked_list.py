class Node:
    
    def __init__(self, label):
        self.__label = label
        self.__next = None

    def getLabel(self):
        return self.__label

    def setLabel(self, label):
        self.__label = label
    
    def getNext(self):
        return self.__next

    def setNext(self, next):
        self.__next = next

class LinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__len_list = 0
    
    def append(self, label, index):
        
        if index >= 0:

            #cria um novo nó
            node = Node(label)

            #verifica se a lista está vazia
            if self.empty():
                self.__first = node
                self.__last = node
            else:
                if index == 0:
                    # inserção no ínicio
                    node.setNext(self.__first)
                    self.__first = node
                elif index >= self.__len_list:
                    # inserção no final
                    self.__last.setNext(node)
                    self.__last = node
                else:
                    # inserção no meio
                    prev_node = self.__first
                    curr_node = self.__first.getNext()
                    curr_index = 1

                    while curr_node != None:

                        if curr_index == index:
                            # seta o curr_node como o próximo do nó
                            node.setNext(curr_node)
                            # seta o node como próximo do prev_node
                            prev_node.setNext(node)
                            break
                        
                        prev_node = curr_node
                        curr_node = curr_node.getNext()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.__len_list += 1

    def remove(self, index):

        if not self.empty() and index >= 0 and index < self.__len_list:
            flag_remove = False

            if self.__first.getNext() == None:
                # possui apenas 1 elemento
                self.__first = None
                self.__last = None
                flag_remove = True
            elif index == 0:
                # remove o ínicio, mas possui mais de 1 elemento
                self.__first = self.__first.getNext()
                flag_remove = True
            else:
                '''
                    Se chegou aqui é porque a lista possui mais de 1 elemento
                    e a remoção não é no início
                '''
                prev_node = self.__first
                curr_node = self.__first.getNext()
                curr_index = 1

                while curr_node != None:
                    # o próximo do anterior aponta para o próximo do nó corrente
                    prev_node.setNext(curr_node.getNext())
                    curr_node.setNext(None)
                    flag_remove = True
                    break 

                prev_node = curr_node
                curr_node = curr_node.getNext()
                curr_index += 1

            if flag_remove:
                #atualiza o tamanho da lista
                self.__len_list -= 1

    def empty(self):
        if self.__first == None:
            return True
        return False
    
    def length(self):
        return self.__len_list

    def show(self):

        curr_node = self.__first

        while curr_node != None:
            print("LinkedList : {}".format(curr_node.getLabel()))
            curr_node = curr_node.getNext()
        print('')


def main():
    linked_list = LinkedList()

    linked_list.append('Python', 0)
    linked_list.append('Javascript', 1)
    linked_list.append('PHP', 0)
    linked_list.append('Ruby', 2)
    linked_list.append('CSS', 4)
    linked_list.append('Mysql', 2)

    linked_list.show()
    print('Tamanho da Lista: {}'.format(linked_list.length()))

    linked_list.remove(0)

    linked_list.show()

    linked_list.remove(0)
    linked_list.remove(2)
    linked_list.remove(0)

    linked_list.show()

    linked_list.append('Java', 8)

    linked_list.show()
    print('Tamanho da Lista: {}'.format(linked_list.length()))


if __name__ == "__main__":
    main()
