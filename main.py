def dfs(start):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return 

  for i in range(start,n):
    if numbers[i] not in s:
      s.append(numbers[i])
      dfs(i+1)
      s.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

s = []

dfs(0)



