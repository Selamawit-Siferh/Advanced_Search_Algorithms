class MiniMaxSearch:
    def __init__(self, state_space_graph):
        self.state_space_graph = state_space_graph

    def minimax(self, state, depth, is_maximizing):
        # Base case: if depth is 0 or the state is a terminal state
        if depth == 0 or not self.state_space_graph[state]["neighbors"]:
            utility = self.state_space_graph[state].get("utility", 0)
            return utility

        if is_maximizing:
            max_eval = -float('inf')
            for neighbor in self.state_space_graph[state]["neighbors"]:
                eval = self.minimax(neighbor, depth - 1, False)
                if eval is not None:
                    max_eval = max(max_eval, eval)
            return max_eval if max_eval != -float('inf') else None
        else:
            min_eval = float('inf')
            for neighbor in self.state_space_graph[state]["neighbors"]:
                eval = self.minimax(neighbor, depth - 1, True)
                if eval is not None:
                    min_eval = min(min_eval, eval)
            return min_eval if min_eval != float('inf') else None

    def find_best_destination(self, start_state, depth):
        best_value = -float('inf')
        best_move = None

        for neighbor in self.state_space_graph[start_state]["neighbors"]:
            value = self.minimax(neighbor, depth - 1, False)
            if value is not None and value > best_value:
                best_value = value
                best_move = neighbor

        return best_move, best_value

# Define the state space graph (terminal nodes have utility values, adversarial nodes do not)
state_space_graph4 = {
"Shambu": {
    "neighbors":["Gedo"],
    "utility": 4
    },
"Fincha": {
    "neighbors":["Gedo"],
    "utility": 5
    },
"Gedo": {
    "neighbors":["Shambu", "Fincha", "Ambo"],
    "utility": None
    },
"Gimbi": {
    "neighbors":["Nekemte"],
    "utility": 8},
"Ambo": {
    "neighbors":["Gedo", "Nekemte", "Addis Ababa"],
    "utility": None
    },
"Addis Ababa": {
    "neighbors":["Ambo", "Buta Jirra", "Adama"],
    "utility": None
    },
"Nekemte": {
    "neighbors":["Gimbi", "Limu", "Ambo"],
    "utility": None
    },
"Limu": {
    "neighbors":["Nekemte"],
    "utility": 8
    },
"Adama": {
    "neighbors":["Addis Ababa", "Mojo", "Dire Dawa"],
    "utility": None
    },
"Buta Jirra": {
    "neighbors":["Addis Ababa", "Worabe", "Wolkite"],
    "utility": None
    },
"Dire Dawa": {
    "neighbors":["Adama", "Harar", "Chiro"],
    "utility": None},
"Harar": {
    "neighbors":["Dire Dawa"],
    "utility": 10
    },
"Chiro": {
    "neighbors":["Dire Dawa"],
    "utility": 6
    },
"Worabe": {
    "neighbors":["Buta Jirra", "Hossana", "Durame"],
    "utility": None
    },
"Wolkite": {
    "neighbors":["Buta Jirra", "Bench Maji", "Tepi"],
    "utility": None
    },
"Hossana": {
    "neighbors":["Worabe"],
    "utility": 6
    },
"Durame": {
    "neighbors":["Worabe"],
    "utility": 5
    },
"Bench Maji": {
    "neighbors":["Wolkite"],
    "utility": 5
    },
"Tepi": {
    "neighbors":["Wolkite"],
    "utility": 6
    },
"Mojo": {
    "neighbors":["Adama", "Kaffa", "Dilla"],
    "utility": None
    },
"Kaffa": {
    "neighbors":["Mojo"],
    "utility": 7
    },
"Dilla": {
    "neighbors":["Mojo"], 
    "utility": 9
    }
}
# Get valid input from the user

minimax_search = MiniMaxSearch(state_space_graph4)
start_state = input("Enter initial state: ")
depth = 3  # Increased depth to allow deeper exploration
best_destination, best_value = minimax_search.find_best_destination(start_state, depth)

print(f"Best destination from {start_state} is {best_destination} with a utility of {best_value}")
