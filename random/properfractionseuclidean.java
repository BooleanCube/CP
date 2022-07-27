import java.io.*;
import java.util.*;

public class properfractionseuclidean {
    
    public static int gcd(int a, int b) {
        if(a==0) return b;
        return gcd(b%a, a);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for(int i=1; i<n; i++)
            if(gcd(i,n) == 1) System.out.println(i + "/" + n);
    }

}
