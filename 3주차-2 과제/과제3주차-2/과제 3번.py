	####회문 검사
	word = input("문자열을 입력하시오: ")

	start = 0
	end = len(word) -1

	while True:
		result = True
	
		if word[start] != word[end]:
			result = False
			break
		start += 1
		end -= 1
		if start > len(word)-1:
			break	

	if result == True:
		print("회문입니다.")
	else:
		print("회문이 아닙니다.")