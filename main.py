from turtle import *
def sieve(number):
    numberList: [int] = [_ for _ in range(2, number)]
    markedList: [int] = []
    completedList: [int] = []
    for i in range(0, number): 
        if numberList[i]**2 >= number:
            lastList = [y for y in numberList if y not in markedList and y not in completedList]
            for i in lastList:
                completedList.append(i)
            break
        if numberList[i] not in markedList:
            completedList.append(numberList[i]) 
        for x in range(numberList.index(numberList[i]**2), len(numberList), numberList[i]): # (Optimisation) Any numbers less than the square will be marked off already. E.g. if 6*6=36, any number smaller than 36 must have another multiple smaller than 6.
            markedList.append(numberList[x]) # We could have done this by looping through each number above the square and checking if the modulo was 0. In doing this with intervals of the number, the multiples are found easier.
            
    return completedList
            

if __name__ == "__main__":
    upTo: int = int(input("Enter the number you want primes to be found up to: "))
    primes = sieve(upTo)
    print(primes);
    increment = 0
