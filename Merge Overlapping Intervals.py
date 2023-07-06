class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        last = -1
        
        ind = 0
        arr = []
        while ind<len(intervals):
            temp = []
            temp.append(intervals[ind][0])
            last = intervals[ind][1]
            ind +=1
            while ind<len(intervals):
                if last>=intervals[ind][0]:
                    last = max(last,intervals[ind][1])
                    ind += 1
                
                else:
                    break
            
            temp.append(last)
            arr.append(temp.copy())
        
        return arr
