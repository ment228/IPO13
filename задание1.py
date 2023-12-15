class Drob(object):
    """ Дробь вида a/b"""

    def __init__(self,m,n):
        self.m = m
        self.n = n
    def __str__(self):
        return f'{self.m}/{self.n}'

    # __eq__
    def __eq__(self, other):
        """ Проверяет равенство двух дробей """
        return self.a == other.a and self.b == other.b
    # __lt__
    def __lt__(self, other):
        """ Проверяет, является ли первая дробь меньше второй """
        return self.a * other.b < other.a * self.b

    def __add__(self, other):
        m1 = self.m * other.n + other.m * self.n
        n1 = self.n * other.n
        return Drob(m1,n1)#сумма
    def __sub__(self, other):
        m1 = self.m * other.n - other.m * self.n
        n1 = self.n * other.n
        return Drob(m1, n1)#вычитание
    def __mul__(self, other):
        m1 = self.m * other.n * other.m * self.n
        n1 = self.n * other.n
        return Drob(m1, n1)#умножение
    def __truediv__(self, other):
        m1 = self.m * other.n / other.m * self.n
        n1 = self.n * other.n
        return Drob(m1, n1)#деление
d1 = Drob(1,3)
d2 = Drob(2,5)
print(f'сумма:{d1}+{d2}={d1+d2}')
print(f'вычитание:{d1}-{d2}={d1-d2}')
print(f'умножение:{d1}*{d2}={d1*d2}')
print(f'деление:{d1}/{d2}={d1/d2}')