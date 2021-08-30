function raceAnalysis(arr,x) {
  if (arr.length==0) {
    return "What A Disaster!!"
  }
  let res=[]
  let boring=true
  for (let i=0; i<arr.length; i++) {
    let s=`${arr[i]-(i+1)}`
    res.push(s>=0 ? "+"+s : s)
    if (res[res.length-1]!="+0") {
      boring=false
    }
  }
  if (boring && arr.length==x) {
    return "Boring Race"
  }
  return [...res, ...Array(x-arr.length).fill("DNF")]
}