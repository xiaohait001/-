num_word=open("词库.txt",'r',encoding="utf-8")
num_word=[num_word.strip() for num_word in num_word.readlines()]
print(num_word)
