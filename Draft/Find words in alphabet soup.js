const genTable = s => {
  return [...s].reduce((prev, cur) => {
    if (!(cur in prev)) {
      prev[cur]=1
    } else {
      prev[cur]+=1
    }
    return prev
  }, {})
}
function numWordsFromSoup(targetStr, soupStr){
  const res=genTable(soupStr.toLowerCase()), origin=genTable(targetStr.toLowerCase())
  return Object.keys(origin).reduce((prev, cur) => Math.min(Math.floor(res[cur]/origin[cur]), prev), Number.MAX_SAFE_INTEGER) || 0
}