class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]

        for num in range(1,numRows):
            temp = []
            for j in range(num+1):
                var = 0
                if j-1>=0:
                    var += answer[num-1][j-1]
                if j<num:
                    var += answer[num-1][j]
                temp.append(var)
            
            answer.append(temp.copy())
        
        return answer
