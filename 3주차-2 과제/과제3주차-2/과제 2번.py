####파일에 사용된 단어의 개수 세기
file_name = input("입력파일 이름 : ")
with open(file_name,"r") as file:
	word_dic = {}
	for i in file:
		i = i.replace(".", " ")
		i = i.replace("'", " ")
		
		for k in i.split():
			if word_dic.get(k) == None:
				word_dic[k] = 1
			else:
				word_dic[k] += 1
	print(word_dic)
