def isAnagram(s1, s2) -> bool:
    if len(s1) != len(s2):
        return False
    
    #return sorted(s1) == sorted(s2) #not the fastest(linear) so we shouldnt do this
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True

#O(NlogN)
#test 
if __name__ == '__main__':
    print(isAnagram('car', 'rac'))
    print(isAnagram('car', 'rca'))
    print(isAnagram('car', 'race'))
    print(isAnagram('car', 'rar'))