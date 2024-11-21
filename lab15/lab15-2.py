class Engine:
    def __init__(self, power, fuel_type):
        self.power = power
        self.fuel_type = fuel_type

    def fuel_consumption(self):
        raise NotImplementedError("Цей метод має бути реалізований в нащадках.")

class InternalCombustionEngine(Engine):
    def __init__(self, power, fuel_type, efficiency):
        super().__init__(power, fuel_type)
        self.efficiency = efficiency

    def fuel_consumption(self):
        return self.power / self.efficiency

class DieselEngine(InternalCombustionEngine):
    def __init__(self, power, fuel_type, efficiency, torque):
        super().__init__(power, fuel_type, efficiency)
        self.torque = torque

    def fuel_consumption(self):
        return super().fuel_consumption() * 1.1

class TurbojetEngine(Engine):
    def __init__(self, power, fuel_type, specific_impulse):
        super().__init__(power, fuel_type)
        self.specific_impulse = specific_impulse

    def fuel_consumption(self):
        return self.power / (self.specific_impulse * 100)

internal_engine = InternalCombustionEngine(200, "petrol", 0.85)
print(f"Витрата палива для двигуна внутрішнього згоряння: {internal_engine.fuel_consumption()} л/год")

diesel_engine = DieselEngine(250, "diesel", 0.9, 400)
print(f"Витрата палива для дизельного двигуна: {diesel_engine.fuel_consumption()} л/год")

turbojet_engine = TurbojetEngine(1000, "aviation fuel", 2500)
print(f"Витрата палива для турбореактивного двигуна: {turbojet_engine.fuel_consumption()} л/год")
