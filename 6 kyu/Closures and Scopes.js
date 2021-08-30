function createFunctions(n) {
  var callbacks = [];
  for (var i=0; i<n; i++) {
    let ans=i
    callbacks.push(function() {return Number(ans)});
  }
  return callbacks;
}