dict={11:"th",12:"th",13:"th",1:"st",2:"nd",3:"rd"}
def number_to_ordinal(n):
    if n>10:
        check=int(str(n)[-2:])
        temp=dict.get(check%10, "th")
        return f"{n}{dict[check]}" if check in dict else f"{n}{temp}"
    else:
        temp=dict.get(n%10, "th")
        return f"{n}{temp}" if n else "0"