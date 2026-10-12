
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quick_sort(left) + middle + quick_sort(right)


n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

print("Sorted array:", quick_sort(arr))
