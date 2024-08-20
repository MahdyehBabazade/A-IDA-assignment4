def idastar(graph, heuristic, start, goal):
    threshold = heuristic[start]
    while True:
        g_score, path = search(graph, heuristic, start, goal, 0, threshold, [start])
        if g_score == float("inf"):
            return -1, []
        elif g_score < 0:
            return -g_score, path
        else:
            threshold = g_score


def search(graph, heuristic, node, goal, g_score, threshold, path):
    if node == goal:
        return -g_score, path
    estimate = g_score + heuristic[node]  # f = g + h
    if estimate > threshold:
        return estimate, path
    min_threshold = float("inf")
    best_path = []
    for neighbor, cost in graph[node].items():
        t, new_path = search(graph, heuristic, neighbor, goal, g_score + cost, threshold, path + [neighbor])
        if t < 0:
            return t, new_path
        elif t < min_threshold:
            min_threshold = t
            best_path = new_path

    return min_threshold, best_path


graph = {
    'a': {'b': 3, 'c': 2},
    'b': {'a': 3, 'd': 4, 'e': 5},
    'c': {'a': 2, 'f': 5},
    'd': {'b': 4},
    'e': {'b': 5},
    'f': {'c': 5, 'g': 1},
    'g': {'f': 1}
}

heuristic = {
    'a': 6,
    'b': 3,
    'c': 4,
    'd': 0,
    'e': 0,
    'f': 1,
    'g': 0
}

result, path = idastar(graph, heuristic, 'a', 'g')
print(f"Cost: {result}, Path: {path}")
