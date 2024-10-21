class StaticArray:
    #TODO: написать спецификацию к структуре данных
    #TODO: реализовать доп свойства
    """
    Имплементация статического массива в Python.

    Здесь и далее будет применяться сокращение arr, обозначающее
    экземпляр типа StaticArray - статический массив.
    ---

    `Атрибуты`
    * `length`   - число элементов arr.
    * `capacity` - размер массива (количество выделенных ячеек для массива arr).

    `Методы`
    * .push(n) - добавить n в конец.
    * .pop() - удалить с конца.
    * .insert(index, value) - добавить value на позицию index.
    * .remove() - удалить элемент на позиции index.


    ---
    `Дополнительные свойства`
    * [x] Вывод массива
    * [ ] Честная индексация
    * [ ] Поддержка метода len
    * [ ] Создание массива при его инициализации
    * [ ] Реализовать ошибки
    """

    length   = 0
    capacity = 0

    def __init__(self, capacity=0):
        self.arr      = []
        self.length   = 0
        self.capacity = capacity
        return None


    def __str__(self):
        output = [str(val) for val in self.arr]
        for i in range(self.capacity - self.length):
            output.append('_')
        return ', '.join(output)


    def push(self, n):
        """Добавить элемент n в конец списка."""
        if self.length < self.capacity:
            self.arr[self.length] = n

            self.length += 1
            return None
        # Тут выбрасывать Out of Bounds


    def pop(self):
        """Удалить последний элемент списка и вернуть его."""
        if self.length > 0:
            element = self.arr[self.length]

            self.length -= 1
            return element
        # Тут выбрасывать Out of Bounds


    def insert(self, index, value):
        """Вставить value на позицию index."""
        if self.length + 1 < self.capacity:
            for i in range(self.length+1, index, -1):
                self.arr[i] = self.arr[i-1]

            self.arr[index] = value
            self.length += 1
            return self.arr
        # Тут выбрасывать Out of Bounds


    #TODO: добавить remove по value легко, нужно пройтись и найти value, затем вызывать метод ниже по его индексу
    def remove(self, index):
        """Удалить элемент на позиции index."""
        if self.length > 0:
            for i in range(index, self.length-1):
                self.arr[i] = self.arr[i+1]

            self.length -= 1
            return self.arr
        # Тут выбрасывать Out of Bounds
    










