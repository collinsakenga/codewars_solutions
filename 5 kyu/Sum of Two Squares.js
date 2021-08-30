function allSquaredPairs(num) {
  let res=[]
  for (let i=0; i<=Math.ceil(Math.sqrt(num)); i++) {
    let pair=Math.sqrt(num-Math.pow(i, 2))
    if (i>pair) {
      break
    }
    if (pair===Math.ceil(pair)) {
      res.push([i, pair])
    }
  }
  return res
}