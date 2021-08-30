table={str(i):i for i in range(10)}

def create_abacus(n):
    res=["---------"]
    num=str(n).rjust(9, "0")
    arr_up, arr_down=["", ""], ["", "", "", "", ""]
    for i in num:
        up, down=table[i]//5, table[i]%5
        for j,k in enumerate(arr_up):
            arr_up[j]+="*" if up==j else " "
        for j,k in enumerate(arr_down):
            arr_down[j]+=" " if down==j else "*"
    return "\n".join(arr_up+res+arr_down)
def read_abacus(abacus):
    arr=abacus.split("\n")
    ans=0
    for j in range(len(arr[0])):
        s="".join(arr[i][j] for i in range(len(arr)))
        up, down=s.split("-")
        ans=ans*10+(up.index("*")*5+down.index(" "))
    return ans