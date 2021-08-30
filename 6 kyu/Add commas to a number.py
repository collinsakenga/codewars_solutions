def commas(num):
    val=round(num, 3)
    return f'{val:,}' if str(val)[-2:]!=".0" else f'{int(val):,}'