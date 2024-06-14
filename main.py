def multiplication ():
    productNums = []
    result = 0
    for i in range (0, rows):
        productNums.append(matrixRowNums[i] * matrixColNums[i])
    result = (productNums[0] + productNums[1])
    return result

columns = 0
rows = 0

rows = int(input("How many rows are there: "))

matrixRowNums = []

print("\nPlease enter the numbers for the rows: ")

for i in range (0, rows):
    nums = int(input())
    matrixRowNums.append(nums)

nums = None

columns = int(input("\nHow many columns are there: "))

print("\nPlease enter the numbers for the Columns: ")

matrixColNums = []
for i in range (0, columns):
    nums = int(input())
    matrixColNums.append(nums)

newlist = []

newlist.append(matrixColNums)
newlist.append(matrixRowNums)

print(matrixRowNums)
print(matrixColNums)

print(multiplication())