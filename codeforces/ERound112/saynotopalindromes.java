//incomplete
import java.io.*;
import java.util.*;

public class saynotopalindromes {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String s = bf.readLine();
        for(int i=0; i<m; i++) {
            st = new StringTokenizer(bf.readLine());
            int l = Integer.parseInt(st.nextToken())-1;
            int r = Integer.parseInt(st.nextToken());
            String sub = s.substring(l, r);
        }
    }
}
