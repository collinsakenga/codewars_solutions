Array.prototype.square=function() {
  let res=[];
  for (let i=0; i<this.length; i++) {
    res.push(this[i]*this[i]);
  }
  return res;
}
Array.prototype.cube=function() {
  let res=[];
  for (let i=0; i<this.length; i++) {
    res.push(this[i]*this[i]*this[i]);
  }
  return res;
}
Array.prototype.sum=function() {
  let res=0;
  for (let i=0; i<this.length; i++) {
    res+=this[i];
  }
  return res;
}
Array.prototype.average=function() {
  let res=0;
  for (let i=0; i<this.length; i++) {
    res+=this[i];
  }
  return res/this.length;
}
Array.prototype.even=function() {
  let res=[];
  for (let i=0; i<this.length; i++) {
    if (this[i]%2==0) {
      res.push(this[i])
    }
  }
  return res;
}
Array.prototype.odd=function() {
  let res=[];
  for (let i=0; i<this.length; i++) {
    if (this[i]%2==1) {
      res.push(this[i])
    }
  }
  return res;
}