def dni_solver(dni):
    table={i:j for i,j in enumerate("TRWAGMYFPDXBNJZSQVHLCKE")}
    return f"{dni[:-1]}{table[int(dni[:-1])%23]}"