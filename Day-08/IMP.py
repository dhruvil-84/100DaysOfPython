"This is an Important Concept used in Caesar Cipher Project"

# Scenerio - I
ls = ['h','e','l','l','o',' ','w','o','r','l','d','!']
for i in ls:
    print(f"Before i = {i}")
    i = 'X'
    print(f"After i = {i}")
print(ls)

'''
when changing the list elements with control variable i of "for i in ls"; the i is changing but it is a copy! IT WILL NOT CHANGE THE ELEMENT OF ORIGINAL LIST.
In this case; to change the original list we have to use a count variable that keeps the track of index of list elements.
'''

# Scenerio - II
for i in range(len(ls)):
    print(f"Before ls[i] = {ls[i]}")
    ls[i] = 'X'
    print(f"After ls[i] = {ls[i]}")
print(ls)

'''
when changing the list elements with control variable i of "for i in range(len(ls))"; the i is index, IT (text[i]) WILL CHANGE THE ELEMENT OF ORIGINAL LIST.
'''