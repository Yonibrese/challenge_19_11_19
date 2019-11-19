sentance = input("write what you want encripted ")
# sentance = "hello there"
shift=int(input("what number do you want to shift by "))
# shift = 4
result = ""
alpha = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQUSTUVWXYZ"
for letter in sentance:
	number_of_letter = alpha.index(letter)
	number_new = number_of_letter + shift
	new_letter = alpha[number_new]
	result += new_letter
print(result)
