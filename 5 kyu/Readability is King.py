def flesch_kincaid(text):
    flag=text.count(".")+text.count("!")+text.count("?")
    text=text.replace("."," ").replace("!"," ")
    length=len(text.split())
    total=0
    for i in text.split():
        total+=syllable(i)
    return round(11.8 *total/length - 15.59 +0.39* length/flag,2)
def syllable(s):
    index=0
    count=0
    while index<len(s):
        if s[index] in "AEIOUaeiou":
            while s[index] in "AEIOUaeiou":
                index+=1
                if index>=len(s):
                    break
            count+=1
        index+=1
    return count
                
                