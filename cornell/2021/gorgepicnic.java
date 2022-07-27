//TLE
//doing a bfs everytime is too slow.

import java.io.*;
import java.util.*;

public class gorgepicnic {
    private static HashMap<Integer, ArrayList<Integer>> tree = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n-1; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(tree.containsKey(a)) tree.get(a).add(b);
            else {ArrayList<Integer> ca=new ArrayList<>();ca.add(b);tree.put(a,ca);}
            if(tree.containsKey(b)) tree.get(b).add(a);
            else {ArrayList<Integer> cb=new ArrayList<>();cb.add(a);tree.put(b,cb);}
        }
        int q = Integer.parseInt(bf.readLine());
        for(int i=0; i<q; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int hiro = Integer.parseInt(st.nextToken());
            int sophie = Integer.parseInt(st.nextToken());
            int des = Integer.parseInt(st.nextToken());
            ArrayList<Integer> h = bfs(hiro, des);
            ArrayList<Integer> s = bfs(sophie, des);
            boolean cube = true;
            for(int idx : h) {
                if(s.contains(idx)) {cube = false; System.out.println("YES"); break;}
            }
            if(cube) System.out.println("NO");
        }
    }

    public static ArrayList<Integer> bfs(int start, int end) {
        Deque<Integer> stack = new ArrayDeque<Integer>();
        HashSet<Integer> visited = new HashSet<>();
        ArrayList<Integer> path = new ArrayList<>();
        int current = start;
        while(current != end) {
            stack.addLast(current);
            
            boolean cube = true;
            for(int n : tree.get(current)) {
                if(!visited.contains(n) && !stack.contains(n)) { cube = false; current = n; break; }
            }
            if(cube) {
                visited.add(current);
                stack.pollLast();
                current = stack.pollLast();
            }
        }
        for(int i : stack) {
            if(i != end) path.add(i);
        }
        return path;
    }
}
