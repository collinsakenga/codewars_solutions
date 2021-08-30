def loose_change(cents):
    cents=int(cents)
    res={'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    if cents<0:
        return res
    if cents>=25:
        res['Quarters']+=cents//25
        cents=cents-res['Quarters']*25
    if cents>=10:
        res['Dimes']+=cents//10
        cents=cents-res['Dimes']*10
    if cents>=5:
        res['Nickels']+=cents//5
        cents=cents-res['Nickels']*5
    if cents>=1:
        res['Pennies']+=cents
    return res