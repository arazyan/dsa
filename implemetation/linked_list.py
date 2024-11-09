class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next  = None


class LinkedList:
    """
    Имплементация односвязного списка в Python.
    
    Здесь и далее будет применяться сокращение linkli, обозначающее
    экземпляр типа LinkedList - односвязный список.

    ---
    `Атрибуты`
    `head`   - первая нода linkli
    `tail`   - последняя нода linkli

    `Методы`
    * add_end(value)  - добавить value в конец списка
    * remove_by_value(value) - удалить value из списка

    `Отличительная особенность`
    В отличие от динамического массива, можно удалить элемент за O(1), если знать его индекс.
    Также, можно добавлять не только в конец, но и в начало за O(1) благодаря атрибуту head.
    С оговоркой, что мы сделаем такую имплементацию, потому что по изначальной логике Linked List не поддерживает
    индексацию т.к. элементы не расположены в памяти последовательно.
    """
    def __init__(self):
        self._dummyNode = ListNode()  # to remember the id of a dummy node
        self.head = self._dummy_node
        self.tail = self.head

    def add_end(self, value):
        """Добавить элемент в конец списка"""
        self.tail.next = ListNode(value)
        self.tail = self.tail.next

    def remove_by_value(self, value):
        """Удалить элемент из списка по значению"""
        # Test Case:
        # link_li = [dummy] 
        # link_li.remove_by_value(value=1), expected_result == -1
        if self.head == self._dummyNode: return -1

        # Test Case:
        # link_li = [dummy, ListNode(1)]
        # link_li.remove_by_value(value=1), expected_result == value
        curr = self.head
        while curr != None:
            next = curr.next
            if next and next.value == value:
                curr.next = next.next
                return value
            curr = next
        return -1
    
    def print(self):
        """Красивый принт списка"""
        curr = self.head.next
        while curr:
            print(f'{curr.value} ->', end=' ')
            curr = curr.next
        print(curr.value)

        