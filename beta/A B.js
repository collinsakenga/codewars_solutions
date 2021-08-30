function howMuchIs(exp){
  let arr=exp.split(" + ")
  let s=(parseInt(arr[0])-parseInt(arr[1])).toString()+(parseInt(arr[0])+parseInt(arr[1])).toString()
  return parseInt(s)
}