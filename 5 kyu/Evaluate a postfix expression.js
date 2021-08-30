function postfixEvaluator(string) {
  stack=[]
  for (let i of string.split(" ")) {
    if (i=="+") {
      let n1=stack.pop(), n2=stack.pop()
      stack.push(n1+n2)
    } else if (i=="-") {
      let n1=stack.pop(), n2=stack.pop()
      stack.push(n2-n1)
    } else if (i=="*") {
      let n1=stack.pop(), n2=stack.pop()
      stack.push(n1*n2)
    } else if (i=="/") {
      let n1=stack.pop(), n2=stack.pop()
      stack.push(Math.floor(n2/n1))
    } else {
      stack.push(+i)
    }
  }
  return stack.pop()
}