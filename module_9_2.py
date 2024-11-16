first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result=[len(string1) for string1 in first_strings if len(string1)>=5]
second_result=[(string1,string2) for string1 in first_strings for string2 in second_strings if len(string1)==len(string2)]
third_strings=first_strings+second_strings
third_result={string3:len(string3) for string3 in third_strings if len(string3)%2==0}
print(first_result)
print(second_result)
print(third_result)