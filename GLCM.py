Mat = [
    [2,1,2,0,1],
    [0,2,1,1,2],
    [0,1,2,2,0],
    [1,2,2,0,1],
    [2,0,1,0,1]
]
colum_num = Mat[:][1].__len__()# the number of the colums
row_num = Mat[1][:].__len__()# the number of the rows
GLCM_0_degreed = [[0 for i in range(3)] for j in range(3)]
GLCM_45_degreed = [[0 for i in range(3)] for j in range(3)]
GLCM_90_degreed = [[0 for i in range(3)] for j in range(3)]
GLCM_135_degreed = [[0 for i in range(3)] for j in range(3)]

#calculate the results for GLCM_0_degreed
x = 0
y = 0
while x<=row_num-1:
    while y<=colum_num-2:
        GLCM_0_degreed[Mat[x][y]][Mat[x][y+1]] = GLCM_0_degreed[Mat[x][y]][Mat[x][y+1]] + 1
        y = y + 1
    x = x + 1
    y = 0

#calculate the results for GLCM_45_degreed
x1 = 1
y1 = 0
while x1<=row_num-1:
    while y1<=colum_num-2:
        GLCM_45_degreed[Mat[x1][y1]][Mat[x1-1][y1+1]] = GLCM_45_degreed[Mat[x1][y1]][Mat[x1-1][y1+1]] + 1
        y1 = y1 + 1
    x1 = x1 + 1
    y1 = 0

#calculate the results for GLCM_90_degreed
x2 = 1
y2 = 0
while x2<=row_num-1:
    while y2<=colum_num-1:
        GLCM_90_degreed[Mat[x2][y2]][Mat[x2-1][y2]] = GLCM_90_degreed[Mat[x2][y2]][Mat[x2-1][y2]] + 1
        y2 = y2 + 1
    x2 = x2 + 1
    y2 = 0

#calculate the results for GLCM_135_degreed
x3 = 0
y3 = 0
while x3<=row_num-2:
    while y3<=colum_num-2:
        GLCM_135_degreed[Mat[x3][y3]][Mat[x3+1][y3+1]] = GLCM_135_degreed[Mat[x3][y3]][Mat[x3+1][y3+1]] + 1
        y3 = y3 + 1
    x3 = x3 + 1
    y3 = 0

print(GLCM_0_degreed)
print(GLCM_45_degreed)
print(GLCM_90_degreed)
print(GLCM_135_degreed)