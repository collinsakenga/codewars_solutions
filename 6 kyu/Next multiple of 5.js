const nextMultipleOfFive = n => {
  let res=n.toString(2)
  let arr=["0", "1"]
  while (true) {
    for (let i of arr) {
      let ans=parseInt(res+i, 2)
      if (ans>0 && ans%5===0) {
        return ans
      }
    }
    let temp=[]
    for (let i of arr) {
      temp.push(i+"0")
      temp.push(i+"1")
    }
    arr=temp
  }
}