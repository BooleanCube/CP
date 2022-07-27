import java.io.*;
import java.util.*;

public class horseshoes {
    
    static Point[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        map = new Point[n][n];
        for(int i=0; i<n; i++) {
            String l = bf.readLine();
            for(int j=0; j<n; j++) {
                map[i][j] = new Point(i, j, l.charAt(j));
            }
        }

    }

}

class Point {
    
    public int x;
    public int y;
    public char val;
    public int counter = 0;
    
    public Point(int x, int y, char v) {
        this.x = x;
        this.y = y;
        val = v;
    }

}
