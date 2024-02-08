test_list = [2, 3, 4, 1, 4, 5, 7, 8, 10, 2, 1, 4, 5, 3, 4, 1,2,3,4,5,6,7,8,9,10, 5, 11,2,  200, 2000, 4, 12020, 2012,2, 2,2,2,2,4]
t = []
final_lists = []
def getIncreasingLists(list):
    results = []
    current = [list[0]]
    for i in range(1, len(list)):
        if list[i-1] <= list[i]:
            current.append(list[i])
        else:
            results.append(current)
            current = [list[i]]
        if i == len(list) - 1:
            results.append(current)
    t = results
    return results 

def sepperateList(results):
    print(results)
    for i in results:
        print(i)
        print(len(i))
        if len(i) >= 4:
            final_lists.append(i)
            print('')
    if len(final_lists) > 3:
        print("this is most liklely to man reps")
    return(final_lists)


print(getIncreasingLists(test_list))
t = getIncreasingLists(test_list)
print("new results")
print(sepperateList(t))
