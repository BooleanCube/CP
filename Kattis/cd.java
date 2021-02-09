import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class cd {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String line = "";
        String[] line1 = {""};
        while (true) {
            line = bf.readLine();
            line1 = line.split(" ");
            int n = Integer.parseInt(line1[0]);
            int m = Integer.parseInt(line1[0]);
            if (n == 0 && m == 0) {
                break;
            }
            int[] a = new int[n];
            int counter = 0;
            for (int i=0; i<n; i++) {
                a[i] = Integer.parseInt(bf.readLine());
            }
            for (int i=0; i<m; i++) {
                if (Arrays.binarySearch(a, Integer.parseInt(bf.readLine())) >= 0) {
                    counter++;
                }
            }
            System.out.println(counter);
        }
    }
}
