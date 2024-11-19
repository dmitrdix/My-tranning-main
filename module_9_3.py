first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result=((len(elem1) - len(elem2)) for elem1, elem2 in zip(first,second) if len(elem1)!=len(elem2))
second_result =((len(first[elem]) == len (second[elem])) for elem in range(len(first)))

print(list(first_result))
print(list(second_result))
