n = int(input())
wall = [[False] * 102 for _ in range(102)]


for i in range(n):
    l, r = map(int, input().split())
    for j in range(l, r):
        wall[i + 1][j] = True

# محاسبه محیط
perimeter = 0
for i in range(1, n + 1):
    for j in range(1, 101):
        if wall[i][j]:
            # چهار جهت
            if not wall[i - 1][j]:
                perimeter += 1
            if not wall[i + 1][j]:
                perimeter += 1
            if not wall[i][j - 1]:
                perimeter += 1
            if not wall[i][j + 1]:
                perimeter += 1

print(perimeter)
