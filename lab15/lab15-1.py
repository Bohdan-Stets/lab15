class Progression:
    def __init__(self, a1, n):
        self.a1 = a1
        self.n = n

    def sum(self):
        raise NotImplementedError("Цей метод має бути реалізований в нащадках.")

class ArithmeticProgression(Progression):
    def __init__(self, a1, n, d):
        super().__init__(a1, n)
        self.d = d

    def sum(self):
        an = self.a1 + (self.n - 1) * self.d
        return (self.n * (self.a1 + an)) / 2

class GeometricProgression(Progression):
    def __init__(self, a1, n, r):
        super().__init__(a1, n)
        self.r = r

    def sum(self):
        if self.r == 1:
            return self.a1 * self.n  # випадок r = 1
        else:
            return self.a1 * (1 - self.r ** self.n) / (1 - self.r)

print("\nВведіть параметри для арифметичної прогресії:")
a1 = int(input("Перший елемент прогресії (a1): "))
n = int(input("Кількість членів прогресії (n): "))
d = int(input("Різниця прогресії (d): "))
r = int(input("Знаменник прогресії (r): "))

arithmetic = ArithmeticProgression(a1, n, d)
print(f"Сума арифметичної прогресії: {arithmetic.sum()}")

geometric = GeometricProgression(a1, n, r)
print(f"Сума геометричної прогресії: {geometric.sum()}")


