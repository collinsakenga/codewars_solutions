def find_missing(sequence):
    sum=(sequence[-1]-sequence[0])//len(sequence)
    return [sequence[index]+sum for index in range(len(sequence)-1) if (sequence[index+1]-sequence[index])!=sum][0]
    
    
