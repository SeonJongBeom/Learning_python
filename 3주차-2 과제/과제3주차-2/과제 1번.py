####파일을 읽고 사용된 단어들 출력하기
file_name = input("입력파일 이름 : ")
with open(file_name,"r") as file:
	word_set = set()
	for i in file:
		i = i.replace(".", " ")
		i = i.replace("'", " ")
		word_set.update(i.split())
	print("사용된 단어의 개수:", len(word_set))
	print(word_set)

