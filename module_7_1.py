from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    str_1 = ''
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        str_1 = file.read()
        file.close()
        return str_1

    def add(self, *products: Product):
        for i in products:
            if i.name not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # str

s1.add(p1, p2, p3)

print(s1.get_products())
