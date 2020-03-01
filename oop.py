class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip()
        if not len(self.name) >= 2:
            raise ValueError('Слишком короткое название товара')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.max_discount = abs(int(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        self.discount = abs(float(discount))
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
        # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def discounted(self):
        return self.price - (self.price * self.discount / 100)

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        raise NotImplementedError


class Phone(Product):
    def __init__(self, name, price, color, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        return f'Цвет корпуса: {self.color}'


class Sofa(Product):
    def __init__(self, name, price, color, texture, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.color = color
        self.texture = texture

    def __repr__(self):
        return f'<Sofa name: {self.name}, price: {self.price}, stock: {self.stock}>'

    def get_color(self):
        return f'Цвет обивки: {self.color}, тип ткани: {self.texture}'


sofa1 = Sofa('Большой диван', 1000, 'Желтый', 'Велюр', discount=25)
print(sofa1)
print(sofa1.get_color())

phone1 = Phone('iPhone Xs', 100, 'Серый')
print(phone1)
print(phone1.get_color())
