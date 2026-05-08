#dictionair
band = {
    "name": "The Beatles",
    "guite": "George Harrison",
}

band2 = dict(name="The Beatles", guite="George Harrison")
print(band)
print(band2)
print(type(band))
#access items
print(band["name"])
print(band.get("name"))

#list all KeyboardInterrupt
print(band.keys())

print(band.get("drummer", "Not found"))

#list all values
print(band.values())

#list of key/value pair as tuples
print(band.items())

#varify a key exists 
print("name" in band)
print("guite" in band)
print("khalid" in band)

#change values
band["guite"] =  "khalid"
band.update({"bass": "paual"})
print(band)

#remove items

print(band.pop("guite"))

print(band.popitem())

print(band)

#delete and clear
band["guite"] = "khalid"
del band["guite"]
print(band)
band.clear()
print(band)

print(band2)

del band2

#copying a dictionary
band2 = band #this is not a copy, it is a reference to the same dictionary
print("Bad copy!")

print(band)

band2["name"] = "dave"

print(band)

band2 = band.copy() #this is a copy, it is a new dictionary with the same key/value pairs
print("Good copy!")
band2["name"] = "dave"
print(band)
print(band2)

# or use the dict constructor function

band3 = dict(band)
print("Good copy!")
print(band3)


#Nested dictionary

member1 = {
    "name": "John Lennon",
    "instrument": "guitar",
}
member2 = {
    "name": "Paul McCartney",
    "instrument": "bass",
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)

print(band["member1"]["name"])

nums = {1,2,3,4,5}

nums2 = set((1,2,3,4,5))


print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates
nums = {1,2,3,4,5,5,5}
print(nums)

#true  is dupe of 1 , false is dupe of 0
nums = {0,1,2,3,4,5, True, False}
print(nums)

#ceck if item exists

print(1 in nums)
print(6 in nums)

#but you can't access items by index
# print(nums[0]) #this will raise an error

# Add items to a set

nums.add(6)
print(nums)

#add elements from another set
morenums = {7,8,9}
nums.update(morenums)
print(nums)

#you can also update  with list , tuple and dictionary

#merge two sets to crete a new set

one = {1,2,3}
two = {3,4,5}
mynewset = one.union(two)
print(mynewset)


#keep only the duplicates
one = {1,2,3}
two = {3,4,5}
one.intersection_update(two)
print(one)

# keep only the except the duplicates

one = {1,2,3}
two = {3,4,5}
one.symmetric_difference_update(two)
print(one)

