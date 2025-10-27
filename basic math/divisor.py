import math as math
def divisor(n):
    temp1 = []
    temp2 = []
    for i in range( 1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            temp1.append(i)
            if i != n // i:
                temp2.append(n // i)
    ans = temp1 + temp2[::-1]
    return ans

div = divisor(36)
print(div)  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]