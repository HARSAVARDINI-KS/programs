print("Enter three Numbers: ")
numOne = int(input())
numTwo = int(input())
numThr = int(input())

if numOne>numTwo:
    if numTwo>numThr:
        large = numOne
    else:
        if numThr>numOne:
            large = numThr
        else:
            large = numOne
else:
    if numTwo>numThr:
        large = numTwo
    else:
        large = numThr

print("\nLargest Number =", large)
