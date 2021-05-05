//incomplete

import java.io.*;
import java.util.*;

public class pumpkinclocktower {
    public static ArrayList<Integer> heights = new ArrayList<Integer>();
    public static HashMap<Integer, ArrayList<Integer>> steadiness = new HashMap<>();
    public static ArrayList<Integer> tower = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int h = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            if(!heights.contains(h)) {
                heights.add(h);
                ArrayList<Integer> ste = new ArrayList<>(); ste.add(s);
                steadiness.put(h, ste);
                tower.add(s);
            } else ste.get(h).add(s);
        }
    }
}
