def solution(args):
    len_args = len(args)
    i = 0
    j = 0
    flag = True
    result = ""
    while True:
        # precondition of i: for i in range(0,len_args-2)
        if i < len_args-2:
            # check if the condition is met
            if args[i+2]-args[i+1] == args[i+1]-args[i] == 1:
                flag = False
                while True:
                    try:
                        # check if the condition is met
                        if args[i+j+2]-args[i+1+j] != args[i+1+j]-args[i+j]:
                            result += str(args[i])+"-"+str(args[i+j+1])+","
                            i = i+j+1
                            break
                    # If index exceeds the range, append result and break
                    except:
                        result += str(args[i])+"-"+str(args[i+j+1])+","
                        i = i+j+1
                        break
                    # iterating the list
                    j += 1
        # append single element to result if the above condition args[i+2]-args[i+1]==args[i+1]-args[i]==1 is not met
        if flag:
            result += str(args[i])+","
        # terminate condition
        if i >= len_args-1:
            # remove excess comma at the end
            return result[:-1]
        # reset variable
        i += 1
        j = 0
        flag = True
