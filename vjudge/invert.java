//not working
import java.util.*;
import java.io.*;

public class invert {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int w = Integer.parseInt(bf.readLine());
        for(int i=0; i<w; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int[] world = new int[c];
            for(int a=0; a<r; a++) {
                char[] line = bf.readLine().toCharArray();
                for(int b=0; b<line.length; b++) if(line[b] == '#') world[k]++;
            }
            boolean norm = true;
            int counter = 0;
            for(int j=0; j<c-1; j++) {
                if((norm == true && world[j+1]-world[j]<k) ||
                   (norm == false && (r-world[j+1])-(r-world[j])<k)) {
                    norm = !norm;
                    ++counter;
                    --j;
                } 
            }
            System.out.println("World #" + i + ": " + counter);
        }
    }
}
