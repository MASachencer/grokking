graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'

processed = set()


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs.keys():
        cost = costs[node]
        # 如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            # 就将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# 在未处理的节点中找出开销最小的节点
node = find_lowest_cost_node(costs)
# while循环在所有节点痘被处理过后结束
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # 遍历当前节点的所有邻居
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # 如果经当前节点前往该邻居更近
        if costs[n] > new_cost:
            # 就更新该邻居的开销
            costs[n] = new_cost
            # 同时将该邻居的父节点设置为当前节点
            parents[n] = node
    # 将当前节点标记为处理过
    processed.add(node)
    # 找出接下来要处理的节点，并循环
    node = find_lowest_cost_node(costs)

print(costs)
