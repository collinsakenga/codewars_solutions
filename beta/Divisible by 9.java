public class DivBy9 {
    public static boolean check(String ns) {
        int total = 0;
        for (char c: ns.toCharArray()) {
            total += Integer.valueOf(String.valueOf(c));}
        return total%9 == 0; }
}