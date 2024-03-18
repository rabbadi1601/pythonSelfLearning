String1="Today is my interview"
tempDict={}
finalDict={}
for i in String1:
    if i in tempDict:
        tempDict[i] +=1
        finalDict.update({i:tempDict[i]})
    elif i!=" ":
        tempDict[i]=1

print(tempDict)
# output: {'T': 1, 'o': 1, 'd': 1, 'a': 1, 'y': 2, 'i': 3, 's': 1, 'm': 1, 'n': 1, 't': 1, 'e': 2, 'r': 1, 'v': 1, 'w': 1}
print(finalDict)
# final result  {'y': 2, 'i': 3, 'e': 2}

print(finalDict.keys())
print(finalDict.values())

# Python3 code to demonstrate
# each occurrence frequency using
# collections.Counter()
from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# using collections.Counter() to get
# count of each element in string
res = Counter(test_str)

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
	+ str(res))

