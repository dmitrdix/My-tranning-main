my_dict={'Дима':1979, 'Алиса' :2007, 'Марина':1983}
print(my_dict)
print(my_dict['Дима'])
print (my_dict.get('Вася'))
my_dict.update({'Алескандр':1954, 'Галина':1955})
my_dict.pop('Алиса')
print (my_dict.get('Алиса',2007))
print(my_dict)
my_set = {1,3,4,5,1,4,'line','get'}
print(my_set)
my_set.update({8,'horror'})
my_set.remove (5)
print(my_set)