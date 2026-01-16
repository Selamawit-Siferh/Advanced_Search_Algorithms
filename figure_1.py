from collections import deque
#import sys

class PathFinder:
    def __init__(self, graph, start_node, goal_node, strategy):
        self.graph = graph
        self.start_node = start_node
        self.goal_node = goal_node
        self.strategy = strategy.strip().lower()
           
    def bfs(self):
        
        visited = []
        queue = deque([(self.start_node, [self.start_node])])
        
        while queue:
            current_node, path = queue.popleft()
            if current_node == self.goal_node:
                return path
            
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def dfs_recursive(self, node, visited=None, path=None):
        if visited is None:
            visited = []
        if path is None:
            path = [node]
        
        if node == self.goal_node:
            return path
        
        visited.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, visited, path + [neighbor])
                if result:
                    return result
        
        return None
    
    def dfs_iterative(self):

        stack = [(self.start_node, [self.start_node])]
        visited = set()
        
        while stack:
            current_node, path = stack.pop()
          
            if current_node == self.goal_node:
                return path
            
            if current_node not in visited:
                visited.add(current_node)
                
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        
        return None
    
    
    def find_path(self):
        if self.strategy == 'bfs':
            return self.bfs()
        elif self.strategy == 'dfs':
            return self.dfs_iterative()
        elif self.strategy == 'dfs recursive':
            return self.dfs_recursive(self.start_node)
        else:
            raise ValueError("Invalid strategy. Use 'bfs', 'dfs', or 'dfs recursive'.")


# Define the graph

state_space_graph = {
    "Kartum": ["Humera", "Metema"],
    "Humera": ["Kartum", "Gondar", "Shire"],
    "Shire": ["Humera", "Debarke", "Axum"],
    "Axum": ["Shire", "Adwa", "Asmera"],
    "Asmera": ["Axum", "Adigrat"],
    "Adigrat": ["Asmera", "Adwa", "Mekelle"],
    "Adwa": ["Axum", "Adigrat", "Mekelle"],
    "Metema": ["Kartum", "Azezo", "Gondar"],
    "Debarke": ["Shire", "Gondar"],
    "Gondar": ["Debarke", "Humera", "Metema", "Azezo"],
    "Azezo": ["Metema", "Gondar", "Bahir Dar"],
    "Mekelle": ["Adwa", "Adigrat", "Sekota", "Alamata"],
    "Sekota": ["Mekelle", "Alamata", "Lalibela"],
    "Alamata": ["Mekelle", "Sekota", "Woldia", "Samara"],
    "Kilbet Rasu": ["Fanti Rasu"],
    "Fanti Rasu": ["Kilbet Rasu", "Samara"],
    "Debre Tabor": ["Bahir Dar", "Lalibela"],
    "Bahir Dar": ["Azezo", "Debre Tabor", "Metekel", "Injibara", "Finote Selam"],
    "Lalibela": ["Debre Tabor", "Sekota", "Woldia"],
    "Woldia": ["Lalibela", "Alamata", "Samara", "Dessie"],
    "Samara": ["Fanti Rasu", "Alamata", "Woldia", "Gabi Rasu"],
    "Metekel": ["Bahir Dar", "Assosa"],
    "Injibara": ["Bahir Dar", "Finote Selam"],
    "Finote Selam": ["Injibara", "Bahir Dar", "Debre Markos"],
    "Debre Markos": ["Finote Selam", "Debre Sina"],
    "Dessie": ["Woldia", "Kemise"],
    "Kemise": ["Dessie", "Debre Sina"],
    "Debre Sina": ["Kemise", "Debre Markos", "Debre Birhan"],
    "Gabi Rasu": ["Samara", "Awash"],
    "Assosa": ["Metekel", "Dembi Dollo"],
    "Debre Birhan": ["Debre Sina", "Addis Ababa"],
    "Dembi Dollo": ["Assosa", "Gambella", "Gimbi"],
    "Gimbi": ["Dembi Dollo", "Nekemte"],
    "Nekemte": ["Gimbi", "Bedelle", "Ambo"],
    "Ambo": ["Nekemte", "Wolkite", "Addis Ababa"],
    "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
    "Adama": ["Addis Ababa", "Batu", "Assella", "Matahara"],
    "Matahara": ["Adama", "Awash"],
    "Awash": ["Matahara", "Gabi Rasu", "Chiro"],
    "Chiro": ["Awash", "Dire Dawa"],
    "Dire Dawa": ["Chiro", "Harar"],
    "Harar": ["Dire Dawa", "Babile"],
    "Babile": ["Harar", "Jigjiga"],
    "Jigjiga": ["Babile", "Dega Habur"],
    "Dega Habur": ["Jigjiga", "Goba", "Kebri Dehar"],
    "Gambella": ["Dembi Dollo", "Gore"],
    "Gore": ["Gambella", "Tepi", "Bedelle"],
    "Bedelle": ["Nekemte", "Gore", "Jimma"],
    "Jimma": ["Bedelle", "Bonga", "Wolkite"],
    "Wolkite": ["Jimma", "Ambo", "Worabe"],
    "Buta Jirra": ["Worabe", "Batu"],
    "Batu": ["Buta Jirra", "Adama", "Shashemene"],
    "Assella": ["Adama", "Assasa"],
    "Tepi": ["Gore", "Mezan Teferi", "Bonga"],
    "Bonga": ["Tepi", "Dawro", "Jimma", "Mezan Teferi"],
    "Hossana": ["Wolaita Sodo", "Shashemene", "Worabe"],
    "Worabe": ["Hossana", "Wolkite", "Buta Jirra"],
    "Shashemene": ["Hossana", "Hawassa", "Batu"],
    "Assasa": ["Assella", "Dodolla"],
    "Mezan Teferi": ["Tepi", "Bonga", "Basketo"],
    "Dawro": ["Bonga", "Basketo", "Wolaita Sodo"],
    "Wolaita Sodo": ["Dawro", "Arba Minch", "Hossana"],
    "Hawassa": ["Shashemene", "Dilla"],
    "Dodolla": ["Shashemene", "Assasa", "Bale"],
    "Bale": ["Dodolla", "Liben", "Goba", "Sof Oumer"],
    "Liben": ["Bale"],
    "Goba": ["Bale", "Sof Oumer", "Dega Habur"],
    "Sof Oumer": ["Bale", "Goba", "Kebri Dehar"],
    "Kebri Dehar": ["Sof Oumer", "Dega Habur", "Werder", "Gode"],
    "Werder": ["Kebri Dehar"],
    "Gode": ["Kebri Dehar", "Dollo", "Mogadishu"],
    "Dollo": ["Gode"],
    "Mogadishu": ["Gode"],
    "Basketo": ["Bench Maji", "Mezan Teferi", "Dawro", "Arba Minch"],
    "Bench Maji": ["Basketo", "Juba"],
    "Juba": ["Bench Maji"],
    "Arba Minch": ["Wolaita Sodo", "Basketo", "Konso"],
    "Dilla": ["Hawassa", "Bule Hora"],
    "Bule Hora": ["Dilla", "Yabello"],
    "Konso": ["Arba Minch", "Yabello"],
    "Yabello": ["Bule Hora", "Konso", "Moyale"],
    "Moyale": ["Yabello", "Nairobi"],
    "Nairobi": ["Moyale"]
}

# Get user input for start and goal nodes
start_node = input("Enter the start node: ").strip().title()
goal_node = input("Enter the goal node: ").strip().title()

# Initialize the search and execute
print("Available search strategies: BFS, DFS, DFS Recursive")
strategy = input("Enter the search strategy: ").strip().lower()
search = PathFinder(state_space_graph, start_node, goal_node, strategy)
solution = search.find_path()
print(f"{strategy.upper()} Solution:", solution)
