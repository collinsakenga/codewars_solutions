public class Hex{
  private int value;
  public Hex(int value){
    this.value=value;
  }
  
  public int valueOf(){
    return value;
  }
  
  public String toJSON(){
    return "0x"+Integer.toHexString(value).toUpperCase();
   }
  
  public String toString(){
    return this.toJSON();
  }
  
  public Hex plus(Hex other){
    return new Hex(this.value+other.value);
  }
  
  public Hex minus(Hex other){
    return new Hex(this.value-other.value);
  }
  
  public Hex plus(int number){
    return new Hex(this.value+number);
  }
  
  public Hex minus(int number){
    return new Hex(this.value-number);
  }
  
  public static int parse(String string){
    if (string.contains("0x")) 
      return Integer.valueOf(string.substring(2), 16).intValue();
    return Integer.valueOf(string, 16).intValue();
  }
  
  public boolean equals(Object other){
    if (other == this) { 
        return true; 
    } 
    if (!(other instanceof Hex)) { 
        return false; 
    } 
    Hex temp = (Hex) other; 
    return temp.value==this.value;
  }
}