import random
def randomSearch(items:list, target) -> int:
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value

    tries = 0

    while True:
        randomIndex = random.randint(0,len(items)-1)
        tries += 1
        if items[randomIndex] == target:
            print("Tries", tries)
            return randomIndex

randomSearch([1,3,5,7,9],7)
def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    checks = 0
    for i in range(len(items)):
        checks += 1
        if items[i] == target:
            return i, checks
    return -1, checks

def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    low = 0
    high = len(items)-1
    checks = 0
    while low <= high:
        mid = int((low+high)/2)
        checks += 1
        if items[mid] == target:
            return mid, checks
        elif items[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1, checks
