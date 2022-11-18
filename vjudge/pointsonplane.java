import java.io.*;
import java.util.*;

public class pointsonplane {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<point> points = new ArrayList<>();
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            point a = new point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), i+1);
            points.add(a);
        }
        Collections.sort(points, (p1, p2) -> Integer.compare(p1.cdist, p2.cdist));
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++) {
            sb.append(points.get(i).idx).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}

class point {
    public int x;
    public int y;
    public int idx;
    public int cdist;
    public int dist() {
        return x*y;
    }
    public point(int x, int y, int idx) {
        this.x = x+1;
        this.y = y+1;
        this.idx = idx;
        this.cdist = this.dist();
    }
}
