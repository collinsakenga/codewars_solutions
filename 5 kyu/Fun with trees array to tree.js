function arrayToTree(array) {
  let res=[]
  for (let i of array) {
    res.push(new TreeNode(i))
  }
  for (let i=0; i<res.length; i++) {
    if ((i*2+1)<res.length) {
      res[i].left=res[i*2+1]
    }
    if ((i*2+2)<res.length) {
      res[i].right=res[i*2+2]
    }
  }
  return res[0]
};