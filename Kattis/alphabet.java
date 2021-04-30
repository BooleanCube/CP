import java.io.*;
import java.io.*;

public class alphabet {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String pat = bf.readLine();
        String alph = "abcdefghijklmnopqrstuvwxyz";
        int m = pat.length();
        int n = alph.length();
        int k[][] = new int[m+1][n+1];
        for (int i=0; i<=m; i++) {
            for (int j=0; j<=n; j++) {
                if (i==0 || j==0) k[i][j] = 0;
                else if (pat.charAt(i-1) == alph.charAt(j-1)) k[i][j] = 1 + k[i-1][j-1];
                else k[i][j] = Math.max(k[i-1][j], k[i][j-1]);
            }
        }
        System.out.println(26-k[m][n]);
    }
}
