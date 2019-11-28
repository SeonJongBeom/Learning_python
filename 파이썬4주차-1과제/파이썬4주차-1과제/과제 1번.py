####
#과제 1번, 사각형의 면적 클래스 생성

class Shape():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	def getArea(self):
		return self.x*self.y
	def getPerimeter(self):
		return 2*(self.x+self.y)

class Rectangle(Shape):
	def __init__(self, height, width, x = 0, y = 0):
		super().__init__(self)
		self.height = height
		self.width = width
	def getArea(self):
		return self.height*self.width
	def getParimeter(self):
		return 2*(self.height + self.width)

a = Rectangle(100,200)
print("사각형의 면적", a.getArea())
print("사각형의 둘레", a.getParimeter())

