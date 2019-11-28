####
#객체지향 3요소 : 캡슐화, 상속, 다형성
#class에는 기능과 필드가 들어가 있어야함
#캡슐화 : 필드와 기능을 묶는것->클래스안의 내용을 하나로 묶는것
#하나로 묶어버려서 안에 뭐가있는지 모르게함. ->캡슐화는 정보은닉 가능
#상속 : 상위 클래스가 하위 클래스한테 상속을 시켜주면 
#하위 클래스로 변수를 선언을 해도 상위 클래스의 값을 불러올 수 있음.
#다형성 : 모습이 같은게 여러개 있을 수 있음.
#단 가까운게 사용됨. ->over riding

####
#counter 클래스
class Counter:
	def reset(self):
		self.count = 0 #인스턴스 변수
	def increment(self):
		self.count += 1
	def get(self):
		return self.count

#객체 생성
a = Counter()
a.reset() #이걸로 카운트를 0으로 초기화 해줌 안해주면 누적 안됨
for i in range(5):
	a.increment()
print("카운터 a의 값은", a.get())

####
#생성자 : 객체가 만들어질때 초기화 시켜줌

class Counter:
	def __init__(self): #클래스 당 하나의 생성자만 허용
		self.count = 0
	def reset(self):
		self.count = 0 #인스턴스 변수
	def increment(self):
		self.count += 1
	def get(self):
		return self.count

#메소드 : 클래스 안에 정의된 함수, 첫 번째 매개변수는 항상 self이어야함.

class Television:
	serialnumber = 0
	Television.serialnumber += 1
	def __init__(self, channel, volume, on):
		self.channel = channel
		self.volume = volume
		self.on = on
	def show(self):
		print(self.channel, self.volume, self.on)
	def setChannel(self, channel):
		self.channel = channel
	def getChannel(self):
		return self.channel
a = Television(1, 1, True)
print(a.channel)

class Student:
	def __init__(self, name = None, age = 0): #age에 값이 안들어 오면 0으로 해줌
		self.__name = name
		self.__age = age
	def getAge(self):
		return self.__age
	def getName(self):
		return self.__name
	def setAge(self, age):
		self.__age=age
	def setName(self, name):
		self.__name = name

obj = Student("Hong", 20)
obj.setName("jongbeom")
print(obj.getName())
obj.setAge(20)
print(obj.getAge())
print(obj.__name)

class Vector2D :
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __add__(self, other): #__add__를 사용하면 클래스끼리의 +연산을 가능 하게 해줌
		return Vector2D(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		return Vector2D(self.x - other.x, self.y - other.y)
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	def __str__(self):
		return '(%g, %g)' % (self.x, self.y)

u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print(a)
if a == w:
	print("같음")
else:
	print("다름")

class Vehicle:
	def __init__(self, make, model, color, price):
		self.make = make # 메이커
		self.model = model # 모델
		self.color = color # 자동차의 색상
		self.price = price # 자동차의 가격
	def setMake(self, make): # 설정자 메소드
		self.make = make
	def getMake(self): # 접근자 메소드
		return self.make
	#차량에 대한 정보를 문자열로 요약하여서 반환한다.
	def getDesc(self):
		return "차량 =("+str(self.make)+","+str(self.model)+","+str(self.color)+","+str(self.price)+")"

class Truck(Vehicle):
	def __init__(self, make, model, color, price, payload):
		super().__init__(make, model, color, price) #super는 상속받는것 상속받는것을 super를 통해서 초기화해줌
		self.payload = payload

	def setPayload(self, payload):
		self.payload = payload
	def getPayload(self):
		return self.payload

myTruck = Truck("Tisla", "Model S", "while", 10000, 2000)
myTruck.setMake("Tesla")
myTruck.setPayload(5000)
print(myTruck.getDesc())
print(myTruck.getPayload())

#클래스 관계
#is - a 상속
#has - a 포함

# 사각형을 클래스로 정의한다.
class Rectangle:
	def __init__(self, side=0):
		self.side = side
	def getArea(self):
		return self.side*self.side
# 사각형 객체와 반복횟수를 받아서 변을 증가시키면서 면적을 출력한다.
def printAreas(r, n):
	while n >= 1:
		print(r.side, "\t", r.getArea())
		r.side = r.side + 1
		n = n - 1

class Animal:
	def __init__(self, name=""):
		self.name=name
	def eat(self):
		print("동물이 먹고 있습니다. ")

class Dog(Animal):
	def __init__(self):
		super().__init__()
	def eat(self):
		print("강아지가 먹고 있습니다. ")

d = Dog();
d.eat()