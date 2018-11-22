"""AULA 13 - Insercaoo por Lista Duplamente Encadeada."""


class ListaDuplaEncadeada():
    """Classe de lista duplamente encadeada."""

    def __init__(self):
        """Inicializador da classe ListaDuplaEncadeada."""
        self.head = self.tail = None

    def insert(self, valor):
        """Insere um elemento No de forma ordenada crescente na lista."""
        # Se lista VAZIA
        if self.head is None:
            self.head = self.tail = No(valor)

        # Se pelo menos um No na lista
        else:
            item = self.head
            while item is not None:
                # Se value do No ATUAL for MAIOR que valor, insere ANTES
                if item.value > valor:
                    novo = No(valor)  # Cria NOVO No
                    novo.next = item
                    novo.previous = item.previous
                    # Se No ATUAL for HEAD (nao existe ANTERIOR)
                    if item == self.head:
                        self.head = novo  # HEAD muda para No NOVO
                    else:  # (existe ANTERIOR)
                        item.previous.next = novo  # proximo do anterior: NOVO
                    item.previous = novo
                    break  # ou return 0  ?
                # Senao, se valor for maior que todos, insere em TAIL
                elif item == self.tail:
                    novo = No(valor)
                    item.next = novo
                    novo.previous = item
                    self.tail = novo
                    break  # ou return 0  ?
                item = item.next

    def show(self):
        """Mostra os valores dos nos da lista."""
        item = self.head
        while item is not None:
            print(item.value)
            item = item.next


class No():
    """Classe do no da lista."""

    def __init__(self, valor):
        """Inicializador da classe No."""
        self.value = valor
        self.next = None
        self.previous = None


def printht(lista):
    """Impressao da lista e seus atributos."""
    if lista.head is not None:
        print("\nHead:{}".format(lista.head.value))
        if lista.head.next is not None:
            print(" Head.Next:{}".format(lista.head.next.value))
        if lista.tail.previous is not None:
            print(" Tail.Prev:{}".format(lista.tail.previous.value))
        print("Tail:{}".format(lista.tail.value))
    lista.show()


li = ListaDuplaEncadeada()

li.insert(4)
li.insert(1)
li.insert(6)
li.insert(5)
li.insert(3)
li.insert(2)
li.insert(7)

printht(li)
