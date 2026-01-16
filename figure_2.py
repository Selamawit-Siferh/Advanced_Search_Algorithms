from queue import PriorityQueue

class MultiGoalRoutePlanner:
    def __init__(self, network):
        self.network = network

    def uniform_cost_search(self, start, goal):
        queue = PriorityQueue()
        queue.put((0, start, [start]))
        visited = set()
        
        while not queue.empty():
            cost, location, path = queue.get()
            
            if location == goal:
                return path, cost
                
            if location not in visited:
                visited.add(location)
                
                for neighbor, travel_cost in self.network.get(location, []):
                    if neighbor not in visited and isinstance(travel_cost, (int, float)):
                        queue.put((cost + travel_cost, neighbor, path + [neighbor]))
        
        return None, None

    def multi_destination_route(self, start, destinations):
        position = start
        remaining = set(destinations)
        full_route = [start]
        total_cost = 0
        journey_details = []
        
        while remaining:
            minimum_cost = float('inf')
            optimal_route = None
            next_destination = None
            
            for destination in remaining:
                route, cost = self.uniform_cost_search(position, destination)
                if route and cost < minimum_cost:
                    minimum_cost = cost
                    optimal_route = route
                    next_destination = destination
            
            if optimal_route is None:
                return None, None, None
            
            journey_details.append((position, next_destination, optimal_route, minimum_cost))
            full_route.extend(optimal_route[1:])
            total_cost += minimum_cost
            position = next_destination  # Change here: update to the next destination
            remaining.remove(next_destination)
        
        return full_route, total_cost, journey_details

state_space_graph2 = {
    "Kartum": [("Humera", 21), ("Metema", 19)],
    "Humera": [("Kartum", 21), ("Gondar", 9), ("Shire", 8)],
    "Shire": [("Humera", 8), ("Debarke", 7), ("Axum", 2)],
    "Axum": [("Shire", 2), ("Adwa", 1), ("Asmera", 5)],
    "Asmera": [("Axum", 5), ("Adigrat", 9)],
    "Adigrat": [("Asmera", 9), ("Adwa", 4), ("Mekelle", 4)],
    "Adwa": [("Axum", 1), ("Adigrat", 4), ("Mekelle", 7)],
    "Metema": [("Kartum", 19), ("Azezo", 7), ("Gondar", 7)],
    "Debarke": [("Shire", 7), ("Gondar", 4)],
    "Gondar": [("Debarke", 4), ("Humera", 9), ("Metema", 7), ("Azezo", 1)],
    "Azezo": [("Metema", 7), ("Gondar", 1), ("Bahir Dar", 7)],
    "Mekelle": [("Adwa", 7), ("Adigrat", 4), ("Sekota", 9), ("Alamata", 5)],
    "Sekota": [("Mekelle", 9), ("Alamata", 6), ("Lalibela", 6)],
    "Alamata": [("Mekelle", 5), ("Sekota", 6), ("Woldia", 3), ("Samara", 11)],
    "Kilbet Rasu": [("Fanti Rasu", 6)],
    "Fanti Rasu": [("Kilbet Rasu", 6), ("Samara", 7)],
    "Debre Tabor": [("Bahir Dar", 4), ("Lalibela", 8)],
    "Bahir Dar": [("Azezo", 7), ("Debre Tabor", 4), ("Metekel", 11), ("Injibara", 4), ("Finote Selam", 6)],
    "Lalibela": [("Debre Tabor", 8), ("Sekota", 6), ("Woldia", 7)],
    "Woldia": [("Lalibela", 7), ("Alamata", 3), ("Samara", 8), ("Dessie", 6)],
    "Samara": [("Fanti Rasu", 7), ("Alamata", 11), ("Woldia", 8), ("Gabi Rasu", 9)],
    "Metekel": [("Bahir Dar", 11)],
    "Injibara": [("Bahir Dar", 4), ("Finote Selam", 2)],
    "Finote Selam": [("Injibara", 2), ("Bahir Dar", 6), ("Debre Markos", 3)],
    "Debre Markos": [("Finote Selam", 3), ("Debre Sina", 17)],
    "Dessie": [("Woldia", 6), ("Kemise", 4)],
    "Kemise": [("Dessie", 4), ("Debre Sina", 6)],
    "Debre Sina": [("Kemise", 6), ("Debre Markos", 17), ("Debre Birhan", 2)],
    "Gabi Rasu": [("Samara", 9), ("Awash", 5)],
    "Assosa": [ ("Dembi Dollo", 12)],
    "Debre Birhan": [("Debre Sina", 2), ("Addis Ababa", 5)],
    "Dembi Dollo": [("Assosa", 12), ("Gambella", 4), ("Gimbi", 6)],
    "Gimbi": [("Dembi Dollo", 6), ("Nekemte", 4)],
    "Nekemte": [("Gimbi", 4), ("Bedelle", ""), ("Ambo", 9)],
    "Ambo": [("Nekemte", 9), ("Wolkite", 6), ("Addis Ababa", 5)],
    "Addis Ababa": [("Debre Birhan", 5), ("Ambo", 5), ("Adama", 3)],
    "Adama": [("Addis Ababa", 3), ("Batu", 4), ("Assella", 4), ("Matahara", 3)],
    "Matahara": [("Adama", 3), ("Awash", 1)],
    "Awash": [("Matahara", 1), ("Gabi Rasu", 5), ("Chiro", 4)],
    "Chiro": [("Awash", 4), ("Dire Dawa", 8)],
    "Dire Dawa": [("Chiro", 8), ("Harar", 4)],
    "Harar": [("Dire Dawa", 4), ("Babile", 2)],
    "Babile": [("Harar", 2), ("Jigjiga", 3),("Goba", 28)],
    "Jigjiga": [("Babile", 3), ("Dega Habur", 5)],
    "Dega Habur": [("Jigjiga", 5),  ("Kebri Dehar", 6)],
    "Gambella": [("Dembi Dollo", 4), ("Gore", 5)],
    "Gore": [("Gambella", 5), ("Tepi", 9), ("Bedelle", 6)],
    "Bedelle": [("Nekemte", ""), ("Gore", 6), ("Jimma", 7)],
    "Jimma": [("Bedelle", 7), ("Bonga", 4), ("Wolkite", 8)],
    "Wolkite": [("Jimma", 8), ("Ambo", 6), ("Worabe", 5)],
    "Buta Jirra": [("Worabe", 2), ("Batu", 2)],
    "Batu": [("Buta Jirra", 2), ("Adama", 4), ("Shashemene", 3)],
    "Assella": [("Adama", 4), ("Assasa", 4)],
    "Tepi": [("Gore", 9), ("Mezan Teferi", 4), ("Bonga", 8)],
    "Bonga": [("Tepi", 8), ("Dawro", 10), ("Jimma", 4), ("Mezan Teferi", 4)],
    "Hossana": [("Wolaita Sodo", 4), ("Shashemene", 7), ("Worabe", 2)],
     "Worabe": [("Hossana", 2), ("Buta Jirra", 2), ("Wolkite", 5)],
    "Shashemene": [("Hossana", 7), ("Hawassa", 1), ("Batu", 3), ("Dodolla", 3)],
    "Assasa": [("Assella", 4), ("Dodolla", 1)],
    "Mezan Teferi": [("Tepi", 4), ("Bonga", 4)],
    "Dawro": [("Bonga", 10), ("Wolaita Sodo", 6)],
    "Wolaita Sodo": [("Dawro", 6), ("Arba Minch", ""), ("Hossana", 4)],
    "Hawassa": [("Shashemene", 1), ("Dilla", 3)],
    "Dodolla": [("Shashemene", 3), ("Assasa", 1), ("Bale", 13)],
    "Bale": [("Dodolla", 13), ("Liben", 11), ("Goba", 18), ("Sof Oumer", 23)],
    "Liben": [("Bale", 11)],
    "Goba": [("Bale", 18), ("Sof Oumer", 6), ("Babile", 28)],
    "Sof Oumer": [("Bale", 23), ("Goba", 6), ("Gode", 23)],
    "Kebri Dehar": [("Dega Habur", 6), ("Werder", 6), ("Gode", 5)],
    "Werder": [("Kebri Dehar", 6)],
    "Gode": [("Kebri Dehar", 5), ("Dollo", 17), ("Mogadishu", 22), ("Sof Oumer", 23)],
    "Dollo": [("Gode", 17)],
    "Mogadishu": [("Gode", 22)],
    "Basketo": [("Bench Maji", 5), ("Arba Minch", 10)],
    "Bench Maji": [("Basketo", 5), ("Juba", 22)],
    "Juba": [("Bench Maji", 22)],
    "Arba Minch": [("Wolaita Sodo", ""), ("Basketo", 10), ("Konso", 4)],
    "Dilla": [("Hawassa", 3), ("Bule Hora", 4)],
    "Bule Hora": [("Dilla", 4), ("Yabello", 3)],
    "Konso": [("Arba Minch", 4), ("Yabello", 3)],
    "Yabello": [("Bule Hora", 3), ("Konso", 3), ("Moyale", 6)],
    "Moyale": [("Yabello", 6), ("Nairobi", 22)],
    "Nairobi": [("Moyale", 22)]
}



planner = MultiGoalRoutePlanner(state_space_graph2)

# Question 2.2: Single goal - Addis Ababa to Lalibela
print("Problem 1: Finding path from Addis Ababa to Lalibela")
print("-" * 50)
path, cost = planner.uniform_cost_search("Addis Ababa", "Lalibela")
if path:
    print("Path found:")
    print(" -> ".join(path))
    print(f"Total cost: {cost}")
else:
    print("No path found!")

print("\n" + "=" * 50 + "\n")

# Question 2.3: Multiple goals
print("Problem 2: Multi-goal path optimization")
print("-" * 50)
start_state = "Addis Ababa"
goal_states = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]

print(f"Starting point: {start_state}")
print("Goals to visit:", ", ".join(goal_states))
print("\nFinding optimal path to visit all locations...")

total_path, total_cost, segments = planner.multi_destination_route(start_state, goal_states)

if total_path:
    print("\nComplete path:")
    print(" -> ".join(total_path))
    print(f"\nTotal cost: {total_cost}")
    
    print("\nPath segments:")
    for start, end, path, cost in segments:
        print(f"\nFrom {start} to {end}:")
        print("Path:", " -> ".join(path))
        print(f"Segment cost: {cost}")
else:
    print("Could not find a valid path to visit all locations!")
