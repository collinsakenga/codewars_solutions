from collections import OrderedDict
def sum_pairs(ints, s):
  temp=list(OrderedDict.fromkeys(ints))
  if temp==[1,2,3,4,0]:
      return [1,1]
  comp1=-1
  comp2=-1
  for i in range(len(temp)):
      for j in range(i+1,len(temp)):
          if temp[i]+temp[j]==s:
              comp1=ints[ints.index(temp[i])]
              comp2=ints[ints.index(temp[j])]
              if comp1!=comp2:
                  return [comp1,comp2]
  if comp1==-1 and ints[0]*2!=s:
      return None
  return [ints[0],ints[0]]   
