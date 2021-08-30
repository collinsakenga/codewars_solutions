// remove key-value pairs where the value is null or undefined
function removeEmpty(object) {
  if (!(typeof object === 'object' && object !== null && !Array.isArray(object))) {
    return {}
  }
  function helper(object) {
    if (!(typeof object === 'object' && object !== null && !Array.isArray(object))) {
      return object===null || object===undefined
    }
    for (let k of Object.keys(object)) {
      if (helper(object[k])) {
        delete object[k];
      }
    }
  }
  helper(object)
  return object
}