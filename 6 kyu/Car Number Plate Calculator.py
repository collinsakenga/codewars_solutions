def find_the_number_plate(id):
    return f"{chr(ord('a')+id//999%26)}{chr(ord('a')+(id//(999*26))%26)}{chr(ord('a')+(id//(999*26*26))%26)}{'{:03d}'.format(id%999+1)}"