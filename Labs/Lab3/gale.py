def GaleShapley(menPrefer ,womenPrefer, pairNum):
    pairs = []
    freeMen = [i for i in range(pairNum)]
    currMen = [-1 for i in range(pairNum)]
    proposed = menPrefer
    while len(freeMen) > 0:
        m = freeMen.pop()
        w = proposed[m].pop(0)
        if currMen[w] == -1:
            pairs.append([m, w])
            currMen[w] = m
        else:
            currM = currMen[w]
            if womenPrefer[w].index(currM) < womenPrefer[w].index(m):
                freeMen.append(m)
            else:
                pairs.remove([currM, w])
                pairs.append([m, w])
                currMen[w] = m
                freeMen.append(currM)
    return pairs

def cmp(list):
    return list[0]

if __name__ == '__main__':
    pairNum = int(input())
    menPrefer = []
    womenPrefer = []
    for i in range(pairNum):
        man = list(map(int, input().split()))
        menPrefer.append(man)
    input()
    for i in range(pairNum):
        woman = list(map(int, input().split()))
        womenPrefer.append(woman)

    result = GaleShapley(menPrefer, womenPrefer, pairNum)
    result.sort(key = cmp)
    print(result)
