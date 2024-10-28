class Stack:
    """
    Имплементация стека в Python на динамическом массиве.

    ---
    `Методы`
    * push(elem) - добавить elem на верхушку стека.
    * pop()      - вытащить последний элемент из стека.
    * top()      - посмотреть на последний элемент стека.

    `Отличительная особенность`
    LIFO - Last In First Out.
    """

    def __init__(self):
        self.stack = []


    def __str__(self):
        return '\n'.join(self.stack[::-1])


    def push(self, elem):
        """Добавить элемент в верхушку стека."""
        self.stack.append(elem)
        return self.stack


    def pop(self):
        """Вытащить верхний элемент из стека."""
        if len(self.stack) > 0:
            return self.stack.pop()


    def top(self):
        """Посмотреть на верхний элемент из стека."""
        if len(self.stack) > 0:
            return self.stack[-1]

