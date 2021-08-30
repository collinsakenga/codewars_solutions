function maxSum(root) {
  if (!root) {
    return 0
  }
  let num=root.value+Math.max(maxSum(root.left), maxSum(root.right))
  return num
}