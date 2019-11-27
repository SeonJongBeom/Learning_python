####문자열의 다양한 함수 사용
a = "hello world! hello python!"

a.split()  #공백 단위로 끊어줌
#반환 값 True or False
a.isalpha()#문자열이 전부 알파벳인지 검사
a.isdigit()#문자열이 전부 숫자인지 검사
a.islower()#문자열이 전부 소문자인지 검사 -> 특수문자나 공백은 건너뜀
a.isupper()#문자열이 전부 대문자인지
a.isspace()#문자열이 전부 스페이스 바인지

#반환 값 True or False
a.startswith("hello")#a와 괄호의 값을 처음 부터 비교해줌 같으면 True 틀리면 False
a.endswith("n!")#a와 괄호의 값을 a는 마지막에서무터 괄호는 처음 것부터 비교해줌 괄호의 값이 다 맞으면 True반환

#반환 값 인덱스
a.find("hello")#해당 문자열의 위치를 원소로 반환 여러개 있을 경우 하나만 찾아줌.
a.rfind("python!")#얜 뒤에서부터 찾아줌

#반환 값 숫자
a.count("hello")#해당 문자열의 개수를 세어줌

a. upper()#대문자로 전부 변환
a.lower()#소문자로 전부 변환
a.capitalize()#첫글자만 대문자로 변환
a.replace("python", "C")#a내의 문자열중 일부를 다른 문자열로 변경
a.strip()#왼쪽 오른쪽 공백 문자 제거