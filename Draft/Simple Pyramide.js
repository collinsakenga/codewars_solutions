pyramid = function(arr) {
  return [...arr.sort().reverse(), ...arr.sort().slice(1)];
}


