####
# 과제 4번, 주석달기

class Animal:						#Animal클래스 생성
	def __init__(self, name=""):	#인스턴스 변수 name초기화
		self.name=name
	def eat(self):					#메소드 eat선언
		print("동물이 먹고 있습니다. ")

class Dog(Animal):					#Animal클래스를 상속받는 Dog 클래스 생성
	def __init__(self):				#Dog클래스의 초기화를 진행하면서 Animal클래스의 초기화도 진행
		super().__init__()
	def eat(self):					#Animal클래스의 eat메소드를 오버라이트 함
		print("강아지가 먹고 있습니다. ")
d = Dog();							#Dog클래스를 갖는 객체 d선언	
d.eat()								#Dog클래스의 eat이 실행됨

class Animal:						#Animal클래스 생성
	def __init__(self, name):		#인스턴스 변수 name 초기화
		self.name = name
	def speak(self):				#speak메소드 선언
		return '알 수 없음'			#메소드 사용시 "알 수 없음"을 반환
class Dog(Animal):					#Animal클래스를 상속받는 Dog클래스 선언
	def speak(self):				#speak 메소드 오버라이트
		return '멍멍!'				#반환값을 대체함
class Cat(Animal):					#Animal클래스를 상속받는 Cat클래스 선언
	def speak(self):				#speak 메소드 오버라이트
		return '야옹!'				#반환값 대체
animalList = [Dog('dog1'), Dog('dog2'),Cat('cat1')]
#각각 Dog클래스와 Cat클래스를 name초깃값만 주고 리스트에 저장
for a in animalList:					#반복될때마다 a라는 객체를 리스트의 클래스에따라 생성
	print (a.name + ': ' + a.speak())	#a객체의 해당 클래스의 name과 speak()메소드의 반환값을 출력

class Car :										#Car객체 생성
	def __init__(self, speed):					#speed를 초기화하는 생성자
		self.speed = speed						#speed를 입력받으면 인스턴스 변수 speed에 넣음
	def setSpeed(self, speed):					#spedd를 받는 메소드
		self.speed = speed
	def getDesc(self):							#차량의 속도를 문자열로 출력하는 메소드
		return "차량 =("+str(self.speed) + ")"
class SportsCar(Car) :							#Car클래스를 상속받는 SportsCar클래스 생성
	def __init__(self, speed, turbo):			#speed와 turbo를 초기화하는 생성자
		super().__init__(speed)					#부모의 speed를 초기화하는 생성자
		self.turbo=turbo						#turbo를 입력받으면 인스턴스 변수 turbo에 값을 넣어줌
	def setTurbo(self, turbo):					#turbo의 값을 받는 메소드
		self.turbo=turbo

obj = SportsCar(100, True)
#SportsCar클래스로 obj객체 생성, 생서자가 100을 speed에  True를 turbo에 넣어줌
print(obj.getDesc())#부모 클래스의 메소드 호출 차량 스피드가 출력됨.
obj.setTurbo(False) #turbo에 False값을 넣어줌
