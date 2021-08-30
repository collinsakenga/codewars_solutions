const arange = arr => {
  let res=[]
  let arr2=arr.filter(n=> !(n.constructor === String)).sort((a, b) => a-b)
  let arr3=arr.filter(n=> n.constructor === String).sort((a, b) => Number(a)-Number(b))
  for (let num of arr2) {
    let last=res[res.length-1]
    if (res.length===0 || (!(last instanceof Array) && last!=num) || (last instanceof Array && last[last.length-1]!=num)) {
      res.push(num)
    } else if (last===num) {
      res[res.length-1]=[last, num]
    } else {
      last.push(num)
    }
  }
  return arr3.length>0 ? [...res, arr3] : res
}