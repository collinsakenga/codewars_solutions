String.prototype.trim = function() {
  let start=0, end=this.length-1
  for (let i=0; i<this.length;i++) {
    if (!(this[i]==" " || this[i]=="\n" || this[i]=="\t" || this[i]=="\r")) {
      break
    }
    start+=1
  }
  for (let i=this.length-1; i>=0;i--) {
    if (!(this[i]==" " || this[i]=="\n" || this[i]=="\t" || this[i]=="\r")) {
      break
    }
    end-=1
  }
  if (start>end) {
    return ""
  }
  return this.substring(start, end+1)
};