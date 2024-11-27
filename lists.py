grocery_list = ['apple' , 'banana', 'mango']

data = ['vinodhini',25, True]   # In this we can put any datatypes like boolean , int

print('apple' in grocery_list)   #True

print(data[0])   #vinodhini 
print(data[-1])   #True

 #if we want to find the index value if it was too large

print(grocery_list.index('mango')) #2



print(grocery_list[0:2])  #['apple', 'banana']
                           #['apple', 'banana', 'mango']
                            #['apple', 'banana']
print(grocery_list[0:])
print(grocery_list[-3:-1])

#To find the length of the list
print (len(data)) #3

grocery_list.append('orange')  #['apple', 'banana', 'mango', 'orange']
print(grocery_list)

grocery_list += ['rice']   #['apple', 'banana', 'mango', 'orange','rice']
print(grocery_list)

print('')

grocery_list.extend(['fish','chicken'])
print(grocery_list)     #['apple', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken']

print('') # ---->it's for space between the lines

grocery_list.extend(data)
print(grocery_list) #['apple', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini', 25, True]

grocery_list.insert(0,'mutton')
print(grocery_list)   #['mutton', 'apple', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini', 25, True]

grocery_list[2:2] = ['pepper','onion']
print(grocery_list)  #['mutton', 'apple', 'pepper', 'onion', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini', 25, True]

grocery_list[1:3] = ['chilli','tomato']
print(grocery_list)  #'mutton', 'chilli', 'tomato', 'onion', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini', 25, True]

#To remove the elements from the list
grocery_list.remove(True)
print(grocery_list)   #['mutton', 'chilli', 'tomato', 'onion', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini', 25]

#To remove the last elememt from the list
print(grocery_list.pop()) 
print(grocery_list)  #25
                    #['mutton', 'chilli', 'tomato', 'onion', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini']


print('')

del grocery_list[0]
print(grocery_list)  #['chilli', 'tomato', 'onion', 'banana', 'mango', 'orange', 'rice', 'fish', 'chicken', 'vinodhini']

data.clear()
print(data)    #[]

# sort--->It will give the lists in alphabetical order
grocery_list.sort()
print(grocery_list)  #['banana', 'chicken', 'chilli', 'fish', 'mango', 'onion', 'orange', 'rice', 'tomato', 'vinodhini']

grocery_list[1:2] = ['Salt']
grocery_list.sort()   #Because of S in upper case it has high priority..
print(grocery_list)  #['Salt', 'banana', 'chilli', 'fish', 'mango', 'onion', 'orange', 'rice', 'tomato', 'vinodhini']

# if we want to print salt as alphabetical wise then 
grocery_list.sort(key = str.lower)
print(grocery_list)   #['banana', 'chilli', 'fish', 'mango', 'onion', 'orange', 'rice', 'Salt', 'tomato', 'vinodhini']





