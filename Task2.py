class Stack:
    def __init__(self, order):
        self.order = order
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст")

    def size(self):
        return len(self.items)

    def check(self):
        for i in range(len(self.order)):
            if self.order[i] == "(" or self.order[i] == "{" or self.order[i] == "[":
                self.items.append(self.order[i])
            elif self.order[i] == ")" or self.order[i] == "}" or self.order[i] == "]":
                if self.is_empty():
                    raise IndexError("Скобочная последовательность неправильна")
                if self.order[i] == ")" and self.items[-1] == "(":
                    self.pop()
                elif self.order[i] == "]" and self.items[-1] == "[":
                    self.pop()
                elif self.order[i] == "}" and self.items[-1] == "{":
                    self.pop()
                else:
                    raise ValueError("Скобочная последовательность неправильна")
            else:
                raise ValueError("Скобочная последовательность неправильна")
        print("Скобочная последовательность правильна")




order = list(input("Введите скобочную последовательность: "))
stack_check = Stack(order)
stack_check.check()
