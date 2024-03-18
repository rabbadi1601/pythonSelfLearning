import random

'''
Linear Search
Linear Search, also known as Sequential Search, is a simple searching algorithm that checks each element in a collection until a match is found. 
It is commonly used on small lists or unsorted data.

Working Principle
The linear search algorithm starts from the beginning of the list and compares each element with the target value. 
If a match is found, the algorithm returns the index of the element. If the entire list is traversed without finding a match, 
the algorithm returns a "not found" indicator.

Strengths and Weaknesses
The main advantage of linear search is its simplicity and ease of implementation. 
It works well for small lists or when the data is unsorted. However, its time complexity is O(n), 
which means the search time increases linearly with the size of the list. For larger datasets, linear search may not be the most efficient option.


'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage
my_list = [5, 2, 9, 1, 7]
target_value = 9
result = linear_search(my_list, target_value)
print(f"Index of {target_value} in the list: {result}")

a=[]
i=0
for i in range(100):
    a.append(random.randrange(1,100))

#print(a)
target_value = 96
result = linear_search(a, target_value)
print(f"Index of {target_value} in the list: {result}")
