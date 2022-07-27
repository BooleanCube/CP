import java.io.*;
import java.util.*;

public class icepath {

    static Point[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int cases = Integer.parseInt(bf.readLine());
        while(cases-- > 0) {

            StringTokenizer st = new StringTokenizer(bf.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            map = new Point[n][m];

            Point start = null;
            for(int i=0; i<n; i++) {
                char[] c = bf.readLine().toCharArray();
                for(int j=0; j<m; j++) {
                    if(c[j] == 'S') start = new Point('S', i, j, 0);
                    map[i][j] = new Point(c[j], i, j, 0);
                }
            }

            System.out.println(bfs(start));

        }
    }

    public static int bfs(Point p) {
        ArrayDeque<Point> q = new ArrayDeque<>();

        q.addLast(p);

        while(!q.isEmpty()) {
            Point current = q.pollFirst();
            if(current.val == 'E') return current.counter;
            int x = current.x; int y = current.y;
            boolean abandonYP = false;
            boolean abandonYM = false;
            boolean abandonXP = false;
            boolean abandonXM = false;
            int c = 0;
            for(int i=1;;i++) {
                if(!abandonYP && isWall(x, y+i)) {
                    Point a = map[x][y+i-1];
                    if(a.counter>0 || (a.x==x && a.y==y)) { abandonYP = true; ++c; }
                    else {
                        a.counter = 1+current.counter;
                        q.addLast(a);
                        abandonYP = true; ++c;
                    }
                }
                if(!abandonYM && isWall(x, y-i)) {
                    Point a = map[x][y-i+1];
                    if(a.counter>0 || (a.x==x && a.y==y)) { abandonYM = true; ++c; }
                    else {
                        a.counter = 1+current.counter;
                        q.addLast(a);
                        abandonYM = true; ++c;
                    }
                }
                if(!abandonXP && isWall(x+i, y)) {
                    Point a = map[x+i-1][y];
                    if(a.counter>0 || (a.x==x && a.y==y)) { abandonXP = true; ++c; }
                    else {
                        a.counter = 1+current.counter;
                        q.addLast(a);
                        abandonXP = true; ++c;
                    }
                }
                if(!abandonXM && isWall(x-i, y)) {
                    Point a = map[x-i+1][y];
                    if(a.counter>0 || (a.x==x && a.y==y)) { abandonXM = true; ++c; }
                    else {
                        a.counter = 1+current.counter;
                        q.addLast(a);
                        abandonXM = true; ++c;
                    }
                }
                if(c==4) break;
            }
        }

        return -1;

    }

    public static boolean isWall(int x, int y) {
        if(x<0 || x>=map.length) return true;
        if(y<0 || y>=map[0].length) return true;
        if(map[x][y].val == 'X') return true;
        return false;
    }

}

class Point {
    public char val;
    public int x;
    public int y;
    public int counter;

    public Point(char v, int x, int y, int c) { 
        val = v;
        this.x = x;
        this.y = y;
        counter = c;
    }
}
