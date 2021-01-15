import java.util.*;
class Converter{
  public static long convert(String word){
    String s=word.toLowerCase();
    HashMap<String, Integer> list=new HashMap<>();
    long res=0;
    int initial=1;
    for (int i = 0; i < s.length(); i++) {
        if (res==0) {
            list.put(s.substring(i, i+1), initial);
            initial=0;
            res=1;
        }
        else {
            if (list.get(s.substring(i, i+1))==null) {
                list.put(s.substring(i, i+1), initial);
                res=res*10+initial;
                if (initial==0) {
                    initial=2;
                } else {
                    initial+=1;
                }
            }
            else {
                res=res*10+list.get(s.substring(i, i+1));
            }
        }
    }
    return res;
  }
}