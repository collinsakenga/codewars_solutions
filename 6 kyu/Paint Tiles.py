def paint_tiles(costs):
    for i in range(len(costs)-2, -1, -1):
        costs[i][0]+=min(costs[i+1][1], costs[i+1][2], costs[i+1][3])
        costs[i][1]+=min(costs[i+1][0], costs[i+1][2], costs[i+1][3])
        costs[i][2]+=min(costs[i+1][1], costs[i+1][0], costs[i+1][3])
        costs[i][3]+=min(costs[i+1][1], costs[i+1][2], costs[i+1][0])
    return min(i for i in costs[0])