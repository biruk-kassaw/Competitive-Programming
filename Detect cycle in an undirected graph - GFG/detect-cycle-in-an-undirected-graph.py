from typing import List
from collections import defaultdict, deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		seen = [False] * V
		
		def dfs(node, parent):
		    seen[node] = True
		    
		    for child in adj[node]:
		        if child == parent:
		            continue
		        if seen[child]:
		            return True
		        if dfs(child, node):
		            return True
		            
		    return False
		    
        for i in range(V):
    	    if seen[i]:
    	        continue
		    if dfs(i, V):
		        return True
		    
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends