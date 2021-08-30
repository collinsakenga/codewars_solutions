def to_pretty(seconds):
    if seconds==0:
        return 'just now'
    num=seconds
    transform=[60,60,24,7]
    time=["second", "minute", "hour", "day"]
    for i,j in enumerate(transform):
        if not num//j:
            return f"{num} {time[i]}s ago" if num>1 else f"a {time[i]} ago" if time[i]!="hour" else f"an hour ago"
        num//=j
    return f"{num} weeks ago" if num>1 else f"a week ago"
        