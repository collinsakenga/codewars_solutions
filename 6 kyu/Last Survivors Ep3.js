function lastSurvivors(arr, nums) {
  for (let i=0; i<arr.length; i++) {
    arr[i]=[...arr[i]]
  }
  const h=arr.length;
  for (let i=0; i<nums.length; i++) {
    for (let j=h-1; j>=0; j--) {
      if (nums[i]>0 && "abcdefghijklmnopqrstuvwxyz".includes(arr[j][i])) {
        arr[j][i]=" ";
        nums[i]-=1;
      }
    }
  }
  let res="";
  for (let i of arr) {
    res+=i.join("");
  }
  return res.split(" ").join("");
}