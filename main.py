BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def isEmpty(self):  # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
        return len(self) == 0

    def push(self, _item):  # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
        self.append(_item)

    def pop(self):  # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):  # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
        if not self.isEmpty():
            return self[-1]

    def size(self):  # size - возвращает количество элементов в стеке.
        return len(self)


def check_ballance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()


if __name__ == '__main__':
    for seq in BALLANCED_LIST + UNBALLANCED_LIST:
        if check_ballance(seq) == True:
            print(f'{seq:<30} Сбалансированно')
        else:
            print(f'{seq:<30} Несбалансированно')