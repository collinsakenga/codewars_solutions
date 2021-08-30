def create_phone_number(n):
    result=""
    for num in n:
        result+=str(num)
    return("("+result[0:3]+") "+result[3:6]+"-"+result[6:10])