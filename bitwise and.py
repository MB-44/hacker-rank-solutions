def countPairs(arr):
    count = 0
    uniqueValue = set(arr)
    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            n = arr[i] & arr[j]
            if n > 0 and (n & (n -1 )) == 0 and n in uniqueValue:
                count += 1
            j += 1
        i += 1
    return count


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = countPairs(arr)
    print(result)
