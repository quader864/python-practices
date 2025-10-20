def coloring(ls):
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            for k in range(len(ls[i][j])):
                if i == 0 or i == len(ls)-1 or j == 0 or j == len(ls[i])-1 or k == 0 or k == len(ls[i][j])-1:
                    ls[i][j][k] = 1
                else:
                    ls[i][j][k] = 0