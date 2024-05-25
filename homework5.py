immutable_var = ('book', 13, True, 'python')
print(immutable_var)
#immutable_var[0] = 12
#тип кортеж не поддерживает переназначение
mutable_list = ['super', 12, False, 'qa', 'kl']
mutable_list[0] = 'noll'
mutable_list[3] = 14
print(mutable_list)