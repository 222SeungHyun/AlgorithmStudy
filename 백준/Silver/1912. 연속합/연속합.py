n = int(input())
arr = list(map(int, input().split()))

maxsum = [arr[0]]

for i in range(n - 1):
    maxsum.append(max(maxsum[i] + arr[i + 1], arr[i + 1]))
    
print(max(maxsum))