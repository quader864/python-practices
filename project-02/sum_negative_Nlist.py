counter=0
k=int(input().strip())
bucket = [0] * k
for i in range(k):
    n = int(input().strip())
    if n:
        bucket[i] = n
for index,a in enumerate(bucket):
    if bucket[index]<0:
        counter+=a
print(counter)