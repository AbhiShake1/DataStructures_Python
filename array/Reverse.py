def reverse(arr) -> None:
    start_index = 0
    end_index = len(arr) - 1
    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1


# O(N)
# test
if __name__ == '__main__':
    list_ = [1, 2, 3, 4, 5, -1, -2]
    reverse(list_)
    print(list_)
