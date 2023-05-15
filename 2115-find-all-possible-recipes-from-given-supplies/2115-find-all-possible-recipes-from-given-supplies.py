class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] = len(ingredient)
            
            for ing in ingredient:
                graph[ing].append(recipe)
        ans = []
        q = deque(supplies)
        recipes = set(recipes)
        
        while q:
            supplie = q.popleft()
            
            if supplie in recipes:
                ans.append(supplie)
                
            for child in graph[supplie]:
                
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
                    
        return ans