function removeZeros(array) {
  let count=0
  for (let i of array) {
    if (i==0) {
      count++
    }
  }
  let index=0
  while (index<array.length-count) {
    if (array[index]===0 || array[index]==="0") {
      let temp=array[index]
      for (let j=index+1; j<array.length; j++) {
        array[j-1]=array[j]
      }
      array[array.length-1]=temp
      if (array[index]!=0) {
        index++
      }
    } else {
      index++
    }
  }
  return array
}