class DynamicArray:
    """
    Имплементация динамического массива в Python.

    Здесь и далее будет применяться сокращение arr, обозначающее
    экземпляр типа DynamicArray - динамический массив.

    ---
    `Атрибуты`
    * `length`   - число элементов arr.
    * `capacity` - размер массива (количество выделенных ячеек для массива arr).

    `Методы`
    * push(n)              - добавить n в конец.
    * pop()                - удалить с конца.
    * insert(index, value) - добавить value на позицию index.
    * remove()             - удалить элемент на позиции index.
    * _resize()            - увеличить размер массива. 


    `Отличительная особенность`
    При переполнении экземпляр увеличивает размер
    массива вдвое, в отличие от статического массива.

    ---
    `Дополнительные свойства`
    * [x] Вывод массива
    * [ ] Честная индексация
    * [ ] Поддержка метода len
    * [ ] Создание массива при его инициализации
    * [ ] Реализовать ошибки
    * [ ] Инкапсулировать переменные класса
    """

    length   = 0
    capacity = [0] * 2

    def __init__(self):
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
        if self.length == self.capacity:
            self.arr._resize()

        self.arr[self.length] = n
        self.length += 1
        return None


    def pop(self):
        """Удалить последний элемент списка и вернуть его."""
        if self.length > 0:
            element = self.arr[self.length]

            self.length -= 1
            return element
        # Тут выбрасывать Out of Bounds


    def insert(self, index, value):
        """Вставить value на позицию index."""
        if not(self.length + 1 < self.capacity):
            self.arr._resize()

        for i in range(self.length+1, index, -1):
            self.arr[i] = self.arr[i-1]

        self.arr[index] = value
        self.length += 1
        return self.arr


    def remove(self, index):
        """Удалить элемент на позиции index."""
        if self.length > 0:
            for i in range(index, self.length-1):
                self.arr[i] = self.arr[i+1]

            self.length -= 1
            return self.arr
        # Тут выбрасывать Out of Bounds


    def _resize(self):
        """Увеличить размер массива, когда он переполнен."""
        double_sized_arr = [None] * len(self.arr)
        for idx, val in enumerate(self.arr):
            double_sized_arr[idx] = val
        self.arr = double_sized_arr

