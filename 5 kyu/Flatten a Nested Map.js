// Flattens an hierarchical map into a single level
function flattenMap(map) {
  return helper(map, "", {})
}
function helper(obj, cur, res) {
  if (Object.prototype.toString.call(obj)!=="[object Object]") {
    res[cur.substring(1)]=obj
    return
  }
  for (let i of Object.keys(obj)) {
    helper(obj[i], cur+"/"+i, res)
  } 
  return res
}