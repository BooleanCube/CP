import java.io.*;
import java.util.*;

public class plusandmultiply { 
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        for(int i=0; i<t; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int n = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            ArrayList<Long> set = new ArrayList<>();
            set.add(1l);
            int idx = 0;
            boolean cube = true;
            while(set.get(idx) <= 10*n) {
                long c = set.get(idx);
                if(c*a==n || c+b==n) {cube=false; System.out.println("Yes"); break;}
                if(!set.contains(c*a)) set.add(c*a);
                if(!set.contains(c+b)) set.add(c+b);
                idx++;
                System.out.println(set.get(idx));
            }
            if(cube) System.out.println("No");
        }
    }
}
