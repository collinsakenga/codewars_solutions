def plant(seed, water, fert, temp):
    if 20<=temp<=30:
        return "".join(water*'-'+fert*seed for i in range(water))
    return '-'*water*water+seed