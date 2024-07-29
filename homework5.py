immutable_var = (1, 2, 3, 'a', 'b', 'c', ['hehe'])
print(immutable_var)
immutable_var[6][0] = 'haha' #кортеж может хранить в себе какие-то изменяемые объекты, хотя сам кортеж изменить нельзя. тут я изменила именно список, потому что иначе вывести всё на экран не получится из-за ошибки
print(immutable_var)
mutable_list = [4, 5, 6, 'd', 'e', 'f', 'lol']
print(mutable_list)
mutable_list [5] = 'kkk'
print(mutable_list)