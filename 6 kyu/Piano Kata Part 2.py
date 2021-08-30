dict={i:j for i,j in enumerate(["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"])}
def which_note(key_press_count):
    num=(key_press_count-1)%88
    return dict[num%12]
    
