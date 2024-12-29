def dfs(adj_list, node, parent, visited, parent_dict):
    # Mark the current node as visited
    visited[node] = True
    parent_dict[node] = parent

    # Traverse all the neighbors of the current node
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(adj_list, neighbor, node, visited, parent_dict)


def root_tree(adj_list, root):
    # Number of nodes in the tree
    n = len(adj_list)

    # A dictionary to store the parent of each node
    parent_dict = {}

    # A visited set to keep track of visited nodes
    visited = [False] * n

    # Perform DFS to root the tree starting from the given root
    dfs(adj_list, root, None, visited, parent_dict)

    return parent_dict


# Example usage
if __name__ == "__main__":
    # Tree represented as an adjacency list
    adj_list = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0],
        3: [1],
        4: [1]
    }

    root = 0  # Choosing node 0 as the root
    parent_dict = root_tree(adj_list, root)

    print("Parent dictionary (rooted tree):", parent_dict)