import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class dnastorage {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n; i++) {
            String dna = bf.readLine();
            dna= dna.replaceAll("[AT]","0").replaceAll("[GC]", "1");
            StringBuilder sb = new StringBuilder();
            for(int j=0; j<dna.length(); j+=7) {
                sb.append((char)Integer.parseInt(dna.substring(j, j+7), 2));
            }
            System.out.println(sb);
        }
    }
}
