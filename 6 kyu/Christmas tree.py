def christmas_tree(h):
    return "\n".join((h-1-i)*" "+(i*2+1)*"*"+(h-1-i)*" " for i in range(h))