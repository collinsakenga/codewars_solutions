function separateTypes(input) {
  let res={}
  for (let i of input) {
    if ((typeof i) in res) {
      res[typeof i].push(i)
    } else {
      res[typeof i]=[i]
    }
  }
  return res
}