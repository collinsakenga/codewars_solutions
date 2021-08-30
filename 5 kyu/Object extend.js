let extend = function(...names) {
  let res={};
  let arr=[]
  for (let i of names) {
    arr.push(i)
  }
  for (let i of arr.reverse()) {
    if (! isObject(i)) {
      continue
    }
    res=Object.assign(res, i)
  }
  return res
}