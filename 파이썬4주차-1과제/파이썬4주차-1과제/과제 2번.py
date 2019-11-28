####
#운송수단 클래스와 상속
class Vehicle:
	def condition(self):
		return "운송수단을 운전합니다."

class Car(Vehicle):
	def condition(self):
		return "자동차를 운전합니다."

class Truck(Vehicle):
	def condition(self):
		return "트럭을 운전합니다."

truck1 = Truck()
truck2 = Truck()
car = Car()

print("truck1:", truck1.condition())
print("truck2:", truck2.condition())
print("car:", car.condition())

