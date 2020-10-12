def mergeCount(list1, list2):
    count = 0
    result = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
            count += len(list1)
    result += list1
    result += list2
    return (count, result)

def sortCount(list):
    length = len(list)
    if length == 1:
        return (0, list)
    else:
        list1 = list[:length // 2]
        list2 = list[length//2:]
        count1, list1 = sortCount(list1)
        count2, list2 = sortCount(list2)
        count, list = mergeCount(list1, list2)
    count += count1 + count2
    return (count, list)

if __name__ == '__main__':
    list = list(map(int, input().split()))
    count = 0
    count, list = sortCount(list)
    print(count)
    print(list)
