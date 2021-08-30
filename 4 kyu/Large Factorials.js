function factorial(n){
  let arr=[1]
  for (let i=1; i<=n; i++) {
    for (let j=0; j<arr.length; j++) {
      arr[j]*=i
    }
    let index=0
    while (true) {
      let num=Math.floor(arr[index]/10)
      arr[index]-=num*10
      if (index==arr.length-1) {
        if (num==0) {
          break
        }
        arr.push(num)
      } else {
        arr[index+1]+=num
      }
      index++
    }  
  }
  return arr.reverse().join("")
}