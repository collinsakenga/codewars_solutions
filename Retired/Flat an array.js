//flat an array in node.js v10
function flat(array, depth){
  if (depth===undefined || isNaN(depth)) {
    return array
  }
  console.log(array, depth)
  return helper(array, [], 0, depth)
}
function helper(arr, res, count, limit) {
  if (count>=limit) {
    return 
  }
  for (let i of arr) {
    if (Array.isArray(i)) {
      helper(i, res, count+1, limit)
    } else {
      res.push(i)
    }
  }
  return res
} 