def has_duplicates(arr) -> bool:
    return len(arr) != len(set(arr))

# O(N) {while converting to set}
# test
if __name__ == '__main__':
    print(has_duplicates([1, 2, 3, 4]))
    print(has_duplicates([1, 2, 3, 4, 2]))