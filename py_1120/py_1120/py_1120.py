#스택 : 처음에 넣은게 나중에 나오고 나중에 넣은게 처음으로 나옴
#큐 : 넣은 순서대로 나옴
####
#튜플 : 값이 변하지 않는 리스트! (맨뒤에 추가는 됨!(새로운 튜플이 만들어 지는거라) 값의 변겅이나 삭제는 안됨)
#세트 : 수학의 집합과 비슷함, 중복되지 않는 값들이 모이며 중복되면 자동으로 제거해줌. 
#		항목간에 순서가 없음(인덱스 안됨)
#set = {1,2,3}->으로 선언(중괄호사용)
number = {2,1,3}
for k in range(6):
	for i in number:
		print(i, end = " ")
	print()

a = {1,2,3,4,5}
b = {6,7,8}
#딕셔너리 : 키와 값이 서로 연결되어져 있는것
#딕셔너리 = {'kim':'0105498513', 'park': '01056461325'} 값이 없으면 none을 반환
#collecntions에서 counter모듈

s = 'naver put off till tomorrow what you can today'
s.split() # 단어별로 잘라서 리스트 생성()안에 넣는 문자로 나뉨 아무것도 안넣으면 ' '이거(스페이스) 기준
a = "as"
a.isalpha() #문자열이 알파벳으로 구성 되있는지
a.isdigit() #문자열이 숫자로 구성되어 있는지

s.upper() #문자열을 전부 대문자로
s.lower() #문자열을 전부 소문자로
s.capitalize() # 첫문자만 전부 대문자로
s.replace("put", "a")#s1을 s2로 하나의 문자를 다른 문자로 바꿀 때
#replace 가 첫번째 것만 바꿔주는지 다 바꿔주는지
a = "aaa aaa aaa aaa"
a.replace("aaa", "ccc")

s.strip() #왼쪽, 오른쪽 공백문자 제거
s.lstrip() # 왼쪽 공백 제거
s.rstrip() # 오른쪽 공백 제거

#join(): 문자열을 이어줌
#result = ''.join(내용) ''안의 문자들로 연결해줌
s = ["a", "b", "c", "d"]
result = ','.join(s)
result #결과 : 'a,b,c,d'

a = 'asd'
b = ""
for  i in range(2, -1, -1):
	b += a[i]
b

####
#파일입출력
#open : 파일 가져오기 open("파일 위치","어떻게 사용할건지") r : 읽기용 w : 쓰기용 rw : 둘다가능

####
#객체 : 객체는 상태와 동작을 가지고 있다.
#객체의 상태는 객체의 속성이다. -> 변수 (필드)
#객체의 동작은 객체가 취할 수 있는 동작(기능)이다. -> 함수 (매소드)
#클래스 : 객체에 대한 설계도를 클래스라고 한다.
#클래스의 주요 3가지
#캡슐화, 상속, 정보은닉
#캡슐화 : 데이터와 알고리즘을 하나로 묶는 것

class Counter:
	def reset(self):
		self.count = 0 #인스턴스 변수
	def increment(self):
		self.count += 1
	def get(self):
		return self.count

a = Counter()
a.reset()
for i in range(5):
	a.increment()
	print("카운터 a의 값은", a.get())


#파이썬 데이터 구조(리스트, 딕셔너리, 튜플, 셋,) 문자열 함수들, 스택, 큐, 파일 입출력, 객체 지향

#p 160