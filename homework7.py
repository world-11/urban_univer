my_dict = {'Ivan':2010, 'Petr':2014, 'Vlad':2011, 'Kirill':2011, 'Nikita':2011, 'Karina':2010}
print('Dict:',my_dict)
print('Existing value:',my_dict.get('Vlad'))
print('Not existing value:',my_dict.get('Makar'))
my_dict['Alex']='2011'
my_dict['Irina']='2011'
a = my_dict.pop('Petr')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

my_set = set(['terra', 11, True, 'cat','money', 11, True, 13, 15, 'cat'])
print('Set:',my_set)
my_set.add('dog')
my_set.add('d9i')
my_set.remove(13)
my_set.update()
print('Modified set:', my_set)