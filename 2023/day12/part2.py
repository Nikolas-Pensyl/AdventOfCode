import multiprocessing as mp
import time

#Initially thought I might have to brute force with multiprocessing
#So after optimizing I decided to play around with multiprocessing vs single
#Multiprocessing = 145 ms
#Singleprocessing = 165 ms

#I also learned a great deal about how lists are pass by reference in python and tuples are not
#What a great adventure improving my python has been during this event


content = open('text.txt').read().strip().splitlines()
content = [(line.split()[0], tuple(map(int, line.split()[1].split(',')))) for line in content]

for i in range(len(content)):
    org = content[i][0]
    orgNum = content[i][1]*5
    input = org
    for j in range(4):
        input += '?'+org
    
    content[i] = (input, orgNum)


def getCombosWrapper(args):
    return getCombos(*args)

cache = {}
def getCombos(input, hash):
    if hash == ():
        return 1 if '#' not in input else 0
    
    if input == '':
        return 1 if hash == () else 0
    
    key = (input, hash)
    if key in cache:
        return cache[key]

    count = 0

    if input[0] in '?.':
        count += getCombos(input[1:], hash)

    if input[0] in '?#':
        if len(input) >= hash[0] and '.' not in input[0:hash[0]] and (hash[0] == len(input) or input[hash[0]] != '#'):
            count += getCombos(input[hash[0] + 1:], hash[1:])

    cache[key] = count
    return count


if __name__ ==  '__main__':
    result = []
    start = time.time()
    with mp.Pool(processes=30) as pool:
        result = pool.map(getCombosWrapper, content)
    total = sum(result)
    end = time.time()
    print("Multiprocessing: ", (end-start)*10**3)
    print("The total is:", total)

    total = 0
    start = time.time()
    for i in content:
        total += getCombos(i[0], i[1])
    end = time.time()
    print("Single Process: ", (end-start)*10**3)
    print("The total is:", total)


    
