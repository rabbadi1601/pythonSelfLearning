'''
https://www.linkedin.com/pulse/searching-algorithms-python-linear-search-binary-ketan-raval-iaw4f
Binary Search
Binary Search is a more efficient searching algorithm that works on sorted lists.
It follows a divide-and-conquer approach and eliminates half of the remaining elements at each step, resulting in a significant reduction in search time.

Working Principle
The binary search algorithm starts by comparing the target value with the middle element of the list.
If they match, the search is successful. If the target value is smaller, the algorithm continues the search on the left half of the list.
 If the target value is larger, the algorithm continues the search on the right half.
 This process is repeated until a match is found or the list is exhausted.
Strengths and Weaknesses
Binary Search has a time complexity of O(log n), which means the search time grows logarithmically with the size of the list.
This makes it significantly faster than linear search for larger datasets. However, binary search requires the list to be sorted beforehand,
which can add an extra step in some cases.Additionally, binary search may not be the best choice for small or unsorted list
'''