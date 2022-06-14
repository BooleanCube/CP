import java.io.*;
import java.util.*;

public class missingletter {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        char[] letters = bf.readLine().toCharArray();
        int prev = 0;
        for(int i=0;;i++) {
            int x = letters[i];
            if(x != prev+1 && i>0) {
                System.out.println((char)(prev+1));
                break;
            }
            prev = x;
        }
    }
}
