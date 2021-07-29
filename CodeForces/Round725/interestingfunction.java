//currently tle
import java.io.*;
import java.util.*;

public class interestingfunction {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int counter = 0;
            while(e>s) {
                int p = s;
                while(true) {
                    if(s%10==9) {s/=10; ++counter;}
                    else break;
                }
                ++counter;
                s = ++p;
            }
            System.out.println(counter);
        }
    }
}
