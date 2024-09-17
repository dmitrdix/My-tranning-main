first = 23
second = 45
third = 38
if first==second==third:
    print ('3')
elif first ==second or second==third or first == third:
    print('2')
else:
    print('0')
    first = 23
    second = 45
    third = 23
    if first == second == third:
        print('3')
    elif first == second or second == third or first == third:
        print('2')
    else:
        print('0')