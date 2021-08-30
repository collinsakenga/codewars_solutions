def how_many_pizzas(n):
    return f'pizzas: {n**2//64}, slices: {(n**2-n**2//64*64)//8}'