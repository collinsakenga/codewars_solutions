function convertQueryToMap(query) {
  if (query.length===0) {
    return {}
  }
  const res={};
  for (let i of query.split("&")) {
    let address=decodeURIComponent(i);
    let [key, ...ans]=address.split("=");
    ans=ans.join("=")
    let keys=key.split(".");
    let cur=res;
    let child;
    for (let [j, k] of Object.entries(keys)) {   
      index=Number(j)
      if (!(k in cur)) {
        child=index===keys.length-1 ? ans : {}
        cur[k] = child;
      } else {
        child=cur[k]
      }
      cur=child
    }
  }
  return res
}