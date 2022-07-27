import java.io.*;
import java.util.*;

public class countingstars {
    static char[][] sky;
    static boolean[][] visited;
    static int starsFound = 0;

    public static void main(String[] args) throws IOException {
         BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
         int c=1;
         String input;
         while((input=bf.readLine()) != null) {
             int row=0;
             int col=0;
             StringTokenizer st = null;
             try {
                 st = new StringTokenizer(input);
                 row = Integer.parseInt(st.nextToken());
                 col = Integer.parseInt(st.nextToken());
             } catch(Exception e) {break;}
             sky = new char[row + 2][col + 2];
             visited = new boolean[row + 2][col + 2];
             for(int i=1; i<row+1; i++) {
                 String str = bf.readLine();
                 for(int j=1; j<col+1; j++) {
                     sky[i][j] = str.charAt(j - 1);
                 }
             }
             for(int i=1; i<row+1; i++) {
                 for(int j=1; j<col+1; j++) {
                     if(sky[i][j] == '-' && !visited[i][j]) {
                         find(i, j);
                         starsFound++;
                     }
                 }
             }
             System.out.println("Case " + c + ": " + starsFound);
             c++;
             starsFound=0;
         }
     }

     public static void find(int i, int j) {
        if(sky[i][j] == '-') visited[i][j]=true;
        if(sky[i+1][j] == '-' && !visited[i+1][j]) find(i+1, j);
        if(sky[i-1][j] == '-' && !visited[i-1][j]) find(i-1, j);
        if(sky[i][j+1] == '-' && !visited[i][j+1]) find(i, j+1);
        if(sky[i][j-1] == '-' && !visited[i][j-1]) find(i, j-1);
    }

}
