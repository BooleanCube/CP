import java.io.*;
import java.util.*;

public class numberspiral {

    public static int[][] map;
    public static direction[] dirs = {direction.right, direction.down, direction.left, direction.up};

    public static boolean isEdge(int x, int y) {
        int n = map.length;
        if(x>=n || y>=n || x<0 || y<0) return true;
        return map[x][y] > 0;
    }

    public static void spiral(int x, int y, int i, direction dir) {
        if(i > Math.pow(map.length, 2)) return;
        if(dir == direction.right) {
            map[x][y] = i;
            if(isEdge(x, y+1)) spiral(x+1, y, i+1, direction.down);
            else spiral(x, y+1, i+1, direction.right);
        }
        else if(dir == direction.down) {
            map[x][y] = i;
            if(isEdge(x+1, y)) spiral(x, y-1, i+1, direction.left);
            else spiral(x+1, y, i+1, direction.down);
        }
        else if(dir == direction.left) {
            map[x][y] = i;
            if(isEdge(x, y-1)) spiral(x-1, y, i+1, direction.up);
            else spiral(x, y-1, i+1, direction.left);
        }
        else if(dir == direction.up) {
            map[x][y] = i;
            if(isEdge(x-1, y)) spiral(x, y+1, i+1, direction.right);
            else spiral(x-1, y, i+1, direction.up);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        map = new int[n][n];
        spiral(0, 0, 1, direction.right);
        printMap();
    }

    public static void printMap() {
        int n = map.length;
        int len = (int)Math.log10(Math.pow(n,2))+1;
        for(int i=0; i<n; i++) {
            int[] nums = map[i];
            for(int j : nums) {
                String p = Integer.toString(j);
                while(p.length() < len) p = " " + p;
                System.out.print(p + " ");
            }
            System.out.println();
        }
    }

}

public enum direction {
    up, down, left, right;
}
