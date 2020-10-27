def miniMaxSum(arr):
  arr_sorted = sorted(arr)
  print(sum(arr_sorted[:4]), end=" ")
  print(sum(arr_sorted[-4:]))
print(miniMaxSum([1,2,3,4,5]))



