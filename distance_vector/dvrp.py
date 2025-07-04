import copy

INFINITY = 999
NODES = ['A', 'B', 'C', 'D']

# Initial cost matrix (direct links only, others are INF)
initial_costs = {
    'A': {'A': 0, 'B': 1,   'C': 3,   'D': INFINITY},
    'B': {'A': 1, 'B': 0,   'C': 1,   'D': 4},
    'C': {'A': 3, 'B': 1,   'C': 0,   'D': 1},
    'D': {'A': INFINITY, 'B': 4, 'C': 1,   'D': 0}
}

def print_routing_table(router, table):
    print(f"\nRouting table for {router}:")
    print("Destination\tCost")
    for dest in NODES:
        print(f"{dest}\t\t{table[dest]}")

def distance_vector_routing(costs):
    routing_tables = copy.deepcopy(costs)

    updated = True
    rounds = 0
    while updated:
        updated = False
        rounds += 1
        print(f"\n--- Round {rounds} ---")
        for node in NODES:
            for neighbor in NODES:
                if neighbor == node or costs[node][neighbor] == INFINITY:
                    continue
                for dest in NODES:
                    # Distance from node to dest via neighbor
                    new_distance = costs[node][neighbor] + routing_tables[neighbor][dest]
                    if new_distance < routing_tables[node][dest]:
                        print(f"[Update] {node} to {dest} via {neighbor}: {routing_tables[node][dest]} -> {new_distance}")
                        routing_tables[node][dest] = new_distance
                        updated = True

    print("\n--- Final Routing Tables ---")
    for node in NODES:
        print_routing_table(node, routing_tables)

if __name__ == "__main__":
    distance_vector_routing(initial_costs)
