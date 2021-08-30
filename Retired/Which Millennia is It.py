def this_millennia_or_last(date):
    prefix, year=date[:-2], date[-2:]
    return f"{prefix}{19 if int(year)>=50 else 20}{year}"