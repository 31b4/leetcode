class Solution:
    def imageSmoother(self, img):
        rows = len(img)
        cols = len(img[0])
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                total_sum = 0
                count = 0

                for l in range(max(0, i-1), min(rows, i+2)):
                    for k in range(max(0, j-1), min(cols, j+2)):
                        total_sum += img[l][k]
                        count += 1

                result[i][j] = total_sum // count

        return result
