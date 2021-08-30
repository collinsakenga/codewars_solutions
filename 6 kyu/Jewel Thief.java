public class Dinglemouse {

  public static int crack(final Safe safe) {
        String[] arr={"L00", "L00", "L00"};
        System.out.println(String.join("-", arr));
        int index=0;
        while (index<3) {
            String[] temp=arr.clone();
            int count=safe.unlock(String.join("-", temp)).length();
            System.out.println(count);
            boolean flag=true;
            for (int i = 0; i < 100; i++) {
                temp[index]=String.format("L%02d", i);
                System.out.println(String.join("-", temp));
                if (safe.unlock(String.join("-", temp)).length()<count) {
                    flag=false;
                    break;
                } else if (safe.unlock(String.join("-", temp)).length()>count) {
                    arr[index]=String.format("L%02d", i);
                    flag=false;
                    break;
                }
            }
            for (int i = 0; i < 100 && flag; i++) {
                temp[index]=String.format("R%02d", i);
                if (safe.unlock(String.join("-", temp)).length()<count) {
                    break;
                } else if (safe.unlock(String.join("-", temp)).length()>count) {
                    arr[index]=String.format("R%02d", i);
                    break;
                }
            } 
            index+=1;
        }
        safe.unlock(String.join("-", arr)); 
        return safe.open();
  }

}