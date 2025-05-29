from dataclasses import dataclass


class MyDict:
    def __init__(self):
        self.keystore = []
        self.valuestore = []
        self.itemstore = []
        self.strstore = ""

    def __setitem__(self, key, value):
        setattr(self, key, value)
        self.keystore.append(key)
        self.valuestore.append(value)
        self.itemstore.append(key)
        self.itemstore.append(value)

    def __delitem__(self, key):
        delattr(self, key)
        self.keystore.remove(key)
        i = 0
        while key in self.itemstore:
            i += 1
            if self.itemstore[i] == key:
                self.itemstore.pop(i)
                delvalue = self.itemstore.pop(i)
        self.valuestore.remove(delvalue)

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        return hasattr(self, key)

    def __dir__(self):
        return dir(self)

    def keys(self):
        return(self.keystore)

    def values(self):
        return(self.valuestore)

    def items(self):
        return(self.itemstore)

    def __str__(self):
        self.strstore = ""
        for i in range(len(self.keystore)):
            self.strstore += str(self.keystore[i]) + " : " + str(self.valuestore[i]) + ", "
        self.strstore = self.strstore[:-2]
        return f"Строковое представление словаря: {self.strstore}"





my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])
print('city' in my_dict)
print(my_dict)
del my_dict['age']
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict)
