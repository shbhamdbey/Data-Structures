# Represent individual element in the  Linklist Class(Node)
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linklist:
# Pointing to the head of the Linklist
    def __init__(self):
        self.head = None
#Insert the Data at the Start Point
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
#Print the Linklist
    def print(self):
        if self.head is None:
            print("Linklist is empty")
            return

        itr = self.head
        illtr = ''

        while itr:
            illtr += str(itr.data) + '-->'
            itr = itr.next
        print(illtr)


if __name__ == '__main__':
     ll = Linklist()
     ll.insert_at_begining(5)
     ll.insert_at_begining(89)
     ll.print()
