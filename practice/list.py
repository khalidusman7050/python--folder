user =  ['khalid', 'mohammad', 'sami', 'ahmed', 'yousef']

data = ['usman', 'khalid', 'mohammad', 'sami', 'ahmed']

emptylist = []

print("khalid" in emptylist)

print(user[0])
print(user[-1])
print(data[0])
print(data[-1])


print(user.index("mohammad"))
print(user[0:2])
print(data[0:])

user.append("myde")
print(user)
user += ['jade', 'sara']
print(user)

user.extend(['jjjd'])
print(user)
user.insert(0, "mamo")
print(user)
user.extend(['jjjd1'])
print(user)

user.pop()
print(user)

user[1:3] = ['may', 'dada']
print(user)
user.remove('mamo')
print(user)
del user[0]
print(user)
del user[0:2]
print(user)
del data[:]
print(data)

user.sort()
print(user)
user.sort(reverse=True)
print(user)
user.reverse()
print(user)

nums = [12,43,3,4,3,5,3,2,2,4,5,4]
#nums.sort(reverse=True)
#print(nums)
print(sorted(nums,reverse=True))

mylist = list([1, "Neil", True])
print(mylist)

mytuple = tuple([2, "khan", True])
print(mytuple)
print(type(mytuple))
print(data.count("khalid"))
