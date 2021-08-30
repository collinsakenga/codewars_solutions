var largestDifference = function(data) {
  let res=[]
  for (let i=0; i<data.length-1; i++) {
    for (let j=0; j<data.length; j++) {
      if (data[j]>=data[i]) {
        res.push(j-i)
      }
    } 
  }
  return Math.max(...res)
};