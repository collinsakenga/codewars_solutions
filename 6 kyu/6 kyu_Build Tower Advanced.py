def tower_builder(n_floors, block_size):
    max_len = block_size[0]+(block_size[0]*2)*(n_floors-1)
    count = block_size[0]
    res = []
    for i in range(n_floors):
        for j in range(block_size[1]):
            temp = " "*((max_len-count)//2)+"*"*count+" "*((max_len-count)//2)
            res.append(temp)
        count += block_size[0]*2
    return res
