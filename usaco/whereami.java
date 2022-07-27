//http://www.usaco.org/index.php?page=viewproblem2&cpid=964
//9/10 test cases right
import java.io.*;

public class whereami {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        String farms = bf.readLine();
        int j = 1;
        int i = 0;
        while(i+j<=n) {
            String c = farms.substring(i, i+j);
            if(count(farms, c) > 1) {++j; i=0;}
            ++i;
        }
        System.out.println(j);
    }
    static int count(String str, String strFind) {
        String bruh = str.replaceAll(strFind, "");
        return (str.length()-bruh.length())/strFind.length();
    }
}
