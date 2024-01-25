from needs import *

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [False]*len(strs)
        tracker = []
        for idx,s in enumerate(strs):
            if visited[idx]:
                continue
            visited[idx] = True
            tracker.append([s])
            for jdx in range(idx+1,len(strs)):
                if visited[jdx] == False and set(strs[jdx]) == set(s):
                    visited[jdx] = True
                    tracker[-1].append(strs[jdx]) 
                        
        return tracker
solution = Solution()
print(solution.groupAnagrams(strs=["eat","tea","tan","ate","nat","bat"]))


