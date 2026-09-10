# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")
def insertionsort(lst):
  for i in range(1, len(lst)):
    key = lst[i]
    j = i-1

    while j >=0 and key < lst[j]:
      lst[j+1] = lst[j]
      j-=1
    lst[j+1] = key

  return lst

lst = []
n = int(input())
for i in range(n):
  lst.append(int(input()))
print(insertionsort(lst))
