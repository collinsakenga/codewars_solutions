def pascals_triangle(n):
  if n==1:
      return [1]
  elif n==2:
      return[ 1,1,1]
  elif n>2:
      result=[1,1,1]
      temp=[]
      total=[1,1,1]
      count=1
      for i in range(2,n):
          for i in range(0,count):
              temp.append(result[i]+result[i+1])
          temp=[1]+temp+[1]
          result=temp
          temp=[]
          total.extend(result)
          count+=1
      return total