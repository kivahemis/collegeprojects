slowa = ['abc','abcd','a','ddddd']
leng = []
for element in slowa:
    leng.append(len(element))

result = list(zip(slowa, leng))
print(result)

#Program pobiera słowa z listy, tworzy pary złożonych z tych słów i ich długości