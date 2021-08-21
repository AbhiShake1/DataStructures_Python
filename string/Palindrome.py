def checkPalindrome(arr) -> bool:
    return arr == arr[::-1] #slicing and reversing

#O(N)
#test
if __name__ == "__main__":
    print(checkPalindrome([1, 2, 3, 2, 1]))
    print(checkPalindrome([1, 2, 3, 2, 2]))