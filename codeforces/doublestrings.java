import java.io.*;
import java.util.*;

public class doublestrings {
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        StringBuilder out = new StringBuilder();
        while(t-- > 0) {
            int n = Integer.parseInt(bf.readLine());
            ArrayList<String> wl = new ArrayList<>();
            HashSet<String> ws = new HashSet<>();
            for(int i=0; i<n; i++) {
                String word = bf.readLine();
                wl.add(word);
                ws.add(word);
            }
            StringBuilder sb = new StringBuilder();
            for(String c : wl) {
                boolean flag = true;
                for(int i=1; i<c.length(); i++) {
                    String pre = c.substring(0, i);
                    String suf = c.substring(i);
                    if(ws.contains(pre) && ws.contains(suf)) {
                        sb.append(1);
                        flag = false;
                        break;
                    }
                }
                if(flag) sb.append(0);
            }
            out.append(sb.toString()).append("\n");
        }
        System.out.println(out.toString());
    }

}
