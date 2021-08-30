def nexus(users):
    return sorted(users.items(), key=lambda x: (abs(x[0]-x[1]), x[0]))[0][0]
    
            