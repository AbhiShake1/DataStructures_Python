def reverse(arr) -> None:
    startIndex = 0
    endIndex = len(arr) - 1
    while startIndex < endIndex:
        arr[startIndex], arr[endIndex] = arr[endIndex], arr[startIndex]
        startIndex += 1
        endIndex -= 1

#O(N)
#test
if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5, -1, -2]
    reverse(list_)
    print(list_)