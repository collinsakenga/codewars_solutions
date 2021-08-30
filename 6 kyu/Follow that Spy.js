res=[]
function findRoutes(routes) {
  helper(routes, "", [], [])
  let s=[]
  for (let i of res) {
    if (s.length===0) {
      s.push(i[0])
      s.push(i[1])
    } else {
      s.push(i[1])
    }
  }
  res.length=0
  return s.join(", ")
}
function helper(routes, cur, arr) {
  if (res.length>0) {
    return
  }
  else if (routes.length===0) {
    res=JSON.parse(JSON.stringify(arr))
    return
  }
  for (let i=0; i<routes.length; i++) {
    if (arr.length===0 || routes[i][0]===cur) {
      arr.push(routes[i])
      helper([...routes.slice(0, i), ...routes.slice(i+1)], routes[i][1], arr)
      arr.pop()
    }
  }
}