function flattenTwoLevels(array) {
  let res=[]
  for (let i of array) {
    if (typeof i==="number") {
      res.push(i)
    } else {
      res.push(helper(i, []))
    }
  }
  return res
}
function helper(arr, res) {
  for (let i of arr) {
    if (typeof i==="number") {
      res.push(i)
    } else {
      helper(i,res)
    }
  }
  return res
}