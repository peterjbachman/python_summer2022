# Homework 4
# Peter Bachman

# Import modules
import random
import time
import matplotlib.pyplot as plt


# Implement selection sort - should be O(n^2) complexity level?


def selection_sort(numList):

    # Create necessary objects
    numList = numList.copy()
    sortList = []

    # Iterate this until numList has no values
    while len(numList) > 0:

        # Add min value of original list to new list
        sortList.append(min(numList))

        # Delete this min value from the original list
        del numList[numList.index(sortList[-1])]

    # Commenting this out so the testing doesn't result in a wild amount of
    # printing
    # return sortList


# Implement a merge sort - should be complexity O(n log(n))?
def merge_sort(numList):

    # Set base case, if length is one or less return that value
    if len(numList) <= 1:
        return numList

    # Find the middle of the list
    middle = len(numList) // 2

    # Create the left and right lists
    leftList = numList[:middle]
    rightList = numList[middle:]

    # Recurse the left and right lists
    merge_sort(leftList)
    merge_sort(rightList)

    # Create index values
    indexLeft = 0
    indexRight = 0
    indexMain = 0

    # While the index values are less than the length of the lists
    # merge them based on which list has the smaller value
    while indexLeft < len(leftList) and indexRight < len(rightList):

        # If the right list has the smaller value, add it to the main list, and
        # increment the right and main index
        if rightList[indexRight] < leftList[indexLeft]:
            numList[indexMain] = rightList[indexRight]
            indexRight += 1
            indexMain += 1

        # Otherwise do the same thing but for the left list
        else:
            numList[indexMain] = leftList[indexLeft]
            indexLeft += 1
            indexMain += 1

    # If the lengths of the lists are different, add the remaining
    # values of the list that is longer at the end
    while indexLeft < len(leftList):
        numList[indexMain] = leftList[indexLeft]
        indexLeft += 1
        indexMain += 1
    while indexRight < len(rightList):
        numList[indexMain] = rightList[indexRight]
        indexRight += 1
        indexMain += 1

    # Return the sorted list
    # Commenting this out so the testing doesn't result in a wild amount of
    # printing
    # return numList


# Test each sorting algorithm
testList1 = list(range(26))
testList2 = list(range(26))
random.shuffle(testList1)
random.shuffle(testList2)

selection_sort(testList1)
merge_sort(testList2)


# Time each sorting algorithm
avgTimeSelection = []
avgTimeMerge = []
sampleSize = [25, 50, 100, 200, 500, 1000, 2000]

for i in sampleSize:

    timesSelection = []
    timesMerge = []

    # Run the tests 100 times
    for j in range(100):
        testListSelection = random.sample(range(-10000, 10001), i)
        testListMerge = random.sample(range(-10000, 10001), i)

        # Time binary sort
        startSelection = time.time()
        selection_sort(testListSelection)

        # Add total time to list
        timesSelection.append(time.time() - startSelection)

        # Now do the same for the merge sort
        startMerge = time.time()
        merge_sort(testListMerge)

        # Add total time to list
        timesMerge.append(time.time() - startMerge)
    avgTimeSelection.append(sum(timesSelection) / i)
    avgTimeMerge.append(sum(timesMerge) / i)

avgTimeSelection
avgTimeMerge

# Write the Graph
fig, ax = plt.subplots()
ax.grid(True)
ax.plot(sampleSize, avgTimeSelection, label='Selection Sort')
ax.plot(sampleSize, avgTimeMerge, label='Merge Sort')
ax.set_xlabel('Sample Size')
ax.set_ylabel('Time')
ax.set_title("Comparing Selection Sort and Merge Sort")
ax.legend()

plt.savefig('/Users/peter/Code/python_summer2022/HW/hw4Plot.pdf')
