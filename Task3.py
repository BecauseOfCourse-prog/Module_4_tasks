class Stack:
    def __init__(self, order):
        self.order = order
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if item == "-":
            self.items.append(self.items[-2] - self.items[-1])
            self.items.pop(-3)
            self.items.pop(-2)
        elif item == "+":
            self.items.append(self.items[-2] + self.items[-1])
            self.items.pop(-3)
            self.items.pop(-2)
        elif item == "*":
            self.items.append(self.items[-2] * self.items[-1])
            self.items.pop(-3)
            self.items.pop(-2)
        elif item == "/":
            self.items.append(self.items[-2] / self.items[-1])
            self.items.pop(-3)
            self.items.pop(-2)
        else:
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

    def print(self):
        print(self.items)


stack = Stack(1)
list_in = input()

length = len(list_in)
chars = []

i = 0
while i < length:
    list_char = ""
    if i < length and "0" <= list_in[i] <= "9":
        while i < length and "0" <= list_in[i] <= "9":
            list_char += list_in[i]
            i += 1
        if list_char != "":
            chars.append(int(list_char))
    elif i < length and (list_in[i] == "*" or list_in[i] == "/" or list_in[i] == "+" or list_in[i] == "-"):
        chars.append(list_in[i])
        i += 1
    else:
        i += 1

for n in range(len(chars)):
    stack.push(chars[n])

stack.print()

