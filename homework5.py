immutable_var=45,56,78,True,56,"string",False
print('КОРТЕЖ',immutable_var) #immutable_var[0]=200
print('Элементы кортежа не могут быть изменены и являются эталоном, т.к. для разных задач требуется сравнивать с эталоном')
print(immutable_var[0:5])
mutable_list=["pen","pensil",'paper',1244,True,56784,'list']
print('СПИСОК',mutable_list)
print('Элементы списка изменятся могут, на элементы  разных типов, также могут заменятся удалятся и добавлятся')
print("Переменная",mutable_list[0],'меняется на')
mutable_list[0]=75946
print(mutable_list[0])
print(mutable_list)
mutable_list.append('juce')
mutable_list.extend(['string'])
print(mutable_list)