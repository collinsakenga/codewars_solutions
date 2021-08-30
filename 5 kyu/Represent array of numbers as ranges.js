// Should return a string representing the ranges
function toRange(arr) {
  const res=[]
  for (let i of [...new Set(arr)].sort((a, b) => a-b)) {
    if (res.length===0 || i!=res[res.length-1][res[res.length-1].length-1]+1) {
      res.push([i])
    } else {
      res[res.length-1].push(i)
    }
  }
  return res.map(range => range.length===1 ? `${range[0]}` : `${range[0]}_${range[range.length-1]}`).join(",")
}

// Should return an array
function toArray(str) {
  if (str.length===0) {
    return []
  }
  const res=[]
  for (let i of str.split(",")) {
    if (!i.includes("_")) {
      res.push(Number(i))
    } else {
      let [low, high]=i.split("_")
      low=Number(low)
      high=Number(high)
      res.push(...[...Array(high-low+1).keys()].map(i => i + low))
    }
  }
  return res
}
