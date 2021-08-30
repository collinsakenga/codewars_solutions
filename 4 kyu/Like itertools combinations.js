function* icombinations(arr, k){
  if (k>arr.length || k<0) {
    return null
  }
  for (let i = 0; i < arr.length; i++) {
    if (k===1) {
      yield [arr[i]]
    } else {
      let temp = icombinations(arr.slice(i + 1, arr.length), k - 1);
      for (let j of temp) {
        yield [arr[i], ...j];
      }
    }
  }
}