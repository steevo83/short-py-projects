def sums(tot):
    nums = []
    summ = 0
    for x in range(1, tot):
        if (x%5 == 0) or (x%3 == 0):
            nums.append(x)
            summ += x
    print(summ)
    #print(nums)

sums(1000)

