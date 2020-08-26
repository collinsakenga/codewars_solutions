def change(s, prog, version):
    temp = s.split("\n")
    temp = temp[0:2]+temp[3:-1]
    temp[0] = 'Program: '+prog
    temp[1] = "Author: g964"
    if not valid_number(temp[2].split(": ")[1]):
        return 'ERROR: VERSION or PHONE'
    temp[2] = "Phone: +1-503-555-0090"
    temp[3] = "Date: 2019-01-01"
    if not valid_version(temp[4].split(": ")[1]):
        return 'ERROR: VERSION or PHONE'
    temp[4] = temp[4] if temp[4].split(
        ": ")[1] == "2.0" else "Version: "+version
    return " ".join(temp)


def valid_number(phone):
    check = phone.split("-")
    if len(check) != 4 or phone[0] != "+":
        return False
    return False if not (check[0][1] == "1" and len(check[0]) == 2 and len(check[1]) == 3 and len(check[2]) == 3 and len(check[3]) == 4) else True


def valid_version(ver):
    return False if ((ver[0] or ver[-1]) not in "1234567890" or ver.count(".") == 0 or ver.count(".") >= 2) else True
