n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))



for i in range(len(arr)-1):
    swapped = False
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True

    if swapped == False:
        break
print(arr)