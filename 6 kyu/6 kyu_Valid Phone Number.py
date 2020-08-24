def validPhoneNumber(phoneNumber):
    return False if phoneNumber[0] != "(" or phoneNumber[4] != ")" or phoneNumber[5] != " " or phoneNumber[9] != "-" or len(phoneNumber) != 14 else True
