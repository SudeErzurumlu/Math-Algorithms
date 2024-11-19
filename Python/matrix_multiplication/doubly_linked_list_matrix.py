class Node:
    """
    Represents a node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    Doubly linked list implementation for storing matrix rows or columns.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """
        Append a value to the linked list.
        :param value: Value to append.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def to_list(self):
        """
        Convert linked list to Python list.
        :return: List representation of the linked list.
        """
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return result

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices represented using doubly linked lists.
    :param matrix1: First matrix as a list of DoublyLinkedLists.
    :param matrix2: Second matrix as a list of DoublyLinkedLists.
    :return: Resultant matrix as a list of lists.
    """
    m = len(matrix1)
    n = len(matrix2)
    p = len(matrix2[0].to_list())
    result = [[0] * p for _ in range(m)]

    for i in range(m):
        row = matrix1[i].to_list()
        for j in range(p):
            col = [matrix2[k].to_list()[j] for k in range(n)]
            result[i][j] = sum(row[k] * col[k] for k in range(n))
    return result

# Example usage
if __name__ == "__main__":
    # Example matrices using doubly linked lists
    matrix1 = [DoublyLinkedList() for _ in range(2)]
    matrix2 = [DoublyLinkedList() for _ in range(2)]
    for row, values in zip(matrix1, [[1, 2], [3, 4]]):
        for value in values:
            row.append(value)
    for row, values in zip(matrix2, [[2, 0], [1, 2]]):
        for value in values:
            row.append(value)

    result = multiply_matrices(matrix1, matrix2)
    print("Resultant Matrix:", result)
