"""Listas encadeadas."""


class ListaEncadeada(object):
    """Define a linked list."""

    def __init__(self):
        """Initialize the linked list."""
        self.head = None
        self.tail = None

    def size(self):
        """Return the number of elements in the linked list."""
        iter = self.head
        size = 0
        while iter is not None:
            size += 1
            iter = iter.proximo
        return size

    def remove(self, valor):
        """Remove all the elements with the given value."""
        iter = self.head
        while iter is not None:
            if iter.dado == valor:
                if iter == self.head:             # valor at HEAD
                    if self.head == self.tail:    # = 1 element (valor)
                        self.head = None
                    else:
                        self.head = iter.proximo  # > 1 element (valor at HEAD)
            elif iter.proximo is not None and iter.proximo.dado == valor:
                if iter.proximo is not self.tail:  # valor not at TAIL
                    iter.proximo = iter.proximo.proximo
                else:                              # valor at TAIL
                    iter.proximo = None
                    self.tail = iter
            iter = iter.proximo

    def removeFirst(self):
        """Remove the first elemente of the linked list."""
        if self.head is None:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.proximo

    def append(self, valor):
        """Append a value at the end of the linked list."""
        if self.tail is None:
            self.head = self.tail = No(valor)
        else:
            self.tail.proximo = No(valor)
            self.tail = self.tail.proximo

    def first(self):
        """Return the first element of the linked list."""
        if self.head is None:
            return None
        else:
            return self.head

    def last(self):
        """Return the last element of the linked list."""
        if self.head is None:
            return None
        else:
            return self.tail

    def pop(self):
        """Remove and return the last element of the linked list."""
        if self.head is None:
            return None
        if self.head == self.tail:
            pop = self.head.dado
            self.head = self.tail = None
            return pop
        iter = self.head
        while iter is not None:
            if iter.proximo == self.tail:
                pop = iter.proximo.dado
                self.tail = iter
            iter = iter.proximo
        return pop

    def addFirst(self, valor):
        """Add a value in the first element of the linked list."""
        if self.head is None:
            self.append(valor)
        else:
            old = self.head
            self.head = No(valor)
            self.head.proximo = old


class No(object):
    """Define a node of the linked list."""

    def __init__(self, valor):
        """Initialize No class."""
        self.dado = valor
        self.proximo = None


li = ListaEncadeada()
print("\nTestes with empty list:")
print("size: {}".format(li.size()))
print("first: {}".format(li.first()))
print("last: {}".format(li.last()))
print("pop: {}".format(li.pop()))
li.removeFirst()
print("removingFirst")

print("\nPopulating list:")
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.append(6)
li.append(2)
li.addFirst(1)
li.addFirst(4)

i = li.head
while i is not None:
    print(i.dado)
    i = i.proximo

print("\nTestes with populated list:")
print("size: {}".format(li.size()))
print("first: {}".format(li.first()))
print("last: {}".format(li.last()))
print("removendo valores iguais a 2")
li.remove(2)
print("size: {}".format(li.size()))
print("first: {}".format(li.first()))
print("last: {}".format(li.last()))
print("pop: {}".format(li.pop()))
li.removeFirst()
print("removingFirst")
# print("pop: {}".format(li.pop()))
# print("pop: {}".format(li.pop()))
# print("pop: {}".format(li.pop()))
# print("pop: {}".format(li.pop()))
# print("pop: {}".format(li.pop()))

i = li.head
while i is not None:
    print(i.dado)
    i = i.proximo

# print(li.first().dado) AttributeError: 'str' object has no attribute 'dado'

print("final test")
iterador = li.first()
while iterador is not None:
    print(iterador.dado)
    iterador = iterador.proximo
