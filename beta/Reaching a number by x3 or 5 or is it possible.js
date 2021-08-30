function solution(n) {
  let res=helper(n)
  if (res.includes("false")) {
    return null
  }
  return res
}
function helper(n) {
  if (n<=0) {
    return "false"
  } else if (n==1) {
    return "1"
  } else if (n%5==1){
    return "(".repeat((Math.floor(n/5)))+helper(1)+") + 5".repeat((Math.floor(n/5)))
  } else if (n%3==0) {
    return "("+helper(Math.floor(n/3))+") * 3"
  } else {
    return "("+helper(n-5)+") + 5"
  }
}