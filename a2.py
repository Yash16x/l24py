class vehicle:
    def _init_(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

bmw=vehicle("BMW",200,100)
print("vehicle name: ",bmw.name)
print("vehicle max speed:",bmw.max_speed)
print("vehicle mileage:",bmw.mileage)
print("\n")
audi=vehicle("Audi",250,150)
print("vehicle name:",audi.name)
print("vehicle max speed:",audi.max_speed)
print("vehicle mileage:",audi.mileage)