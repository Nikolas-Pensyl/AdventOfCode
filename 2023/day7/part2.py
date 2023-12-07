# open the sample file used 
file = open('text.txt') 
  
# read the content of the file opened 
content = file.readlines()
content = [[l.split()[0], int(l.split()[1])] for l in content]
total = 0

cardRank = 'AKQT98765432J'

def getType(cards):
    cardsDict = {}
    for c in cards:
        if cardsDict.get(c, -1) == -1:
            cardsDict[c] = 1
        else:
            cardsDict[c] += 1
    
    
    jockerNum = cardsDict.get("J", -1)
    totals = list(cardsDict.values())
    if jockerNum != -1 and jockerNum != 5:
        cardsDict.pop("J")
        totals = list(cardsDict.values())
        totals[totals.index(max(totals))] += jockerNum
    
    
    if max(totals) == 5:
        return 6
    elif max(totals) == 4:
        return 5
    elif 2 in totals and 3 in totals:
        return 4
    elif 3 in totals:
        return 3
    elif totals.count(2) == 2:
        return 2
    elif 2 in totals:
        return 1
    return 0

def lessThanOrEqual(left, right):
    leftHand = getType(left)
    rightHand = getType(right)
    
    if leftHand != rightHand:
        return leftHand <= rightHand
    
    for c in range(len(left)):
        if left[c] != right[c]:
            return cardRank.find(left[c]) > cardRank.find(right[c])
    
    return True

# Function to find the partition position
def partition(array, low, high):
 
    # Choose the rightmost element as pivot
    pivot = array[high]
 
    # Pointer for greater element
    i = low - 1
 
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if lessThanOrEqual(array[j][0], pivot[0]):
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with
    # the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
 
# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)

quicksort(content, 0, len(content)-1)

for i in range(len(content)):
    total += (i+1)*content[i][1]

print(total)
