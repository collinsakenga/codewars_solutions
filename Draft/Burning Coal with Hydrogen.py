# Make sure that hydrogen reacts first
# output should be 
#'X molecules of Water and Y molecules of Carbon dioxide'
def burner(c,h,o):
    temp=min(h//2, o)
    h-=temp*2
    o-=temp
    temp2=min(c, o//2)
    return f'{temp} molecules of Water and {temp2} molecules of Carbon dioxide'