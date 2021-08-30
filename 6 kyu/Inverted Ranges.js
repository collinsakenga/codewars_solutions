function invertedRanges(ranges) {
  if (ranges.length===0) {
    return [[0, 100]]
  } 
  let res=[]
  if (ranges[0][0]>0) {
    res.push([0, ranges[0][0]-1])
  }
  for (let i=0; i<ranges.length-1; i++) {
    let left=ranges[i][1], right=ranges[i+1][0]
    if (right-left>=2) {
      res.push([left+1, right-1])
    }
  }
  if (ranges[ranges.length-1][1]<100) {
    res.push([ranges[ranges.length-1][1]+1, 100])
  }
  return res
}