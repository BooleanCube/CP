import java.io.*;
import java.util.*;

public class binarystrings {
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        while(t-- > 0) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            long n = Long.parseLong(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(bf.readLine());
            long m = 1;
            while(n-- > 0) {
                long num = Long.parseLong(st.nextToken());
                long o = num;
                long counter = 0;
                while(num != o || counter == 0) {
                    num = (num >> 1) + (num&1)*(1 << (k-1));
                    ++counter;
                }
                m = (m*counter) % (long)(Math.pow(10, 9)+7);
            }
            System.out.println(m);
        }
    }
    
}
