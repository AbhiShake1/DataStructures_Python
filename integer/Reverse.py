def reverse(int_: int) -> int:
    reversed_ = 0

    neg = False

    if int_ < 0:
        int_ = -int_
        neg = True

    while int_ > 0:
        rem = int_ % 10
        reversed_ = reversed_ * 10 + rem
        int_ = int_ // 10

    if neg:
        reversed_ = -reversed_

    return reversed_


# O(N)
# test
if __name__ == "__main__":
    print(reverse(1023))
    print(reverse(-1023))
