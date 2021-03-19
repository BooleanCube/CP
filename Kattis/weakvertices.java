import java.io.*;
import java.util.*;

public class weakvertices {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = 0;
        while((n=Integer.parseInt(bf.readLine())) != -1) {
            int[][] graph = new int[n][n];
            ArrayList<Node> nodes = new ArrayList<>();
            for(int i=0; i<n; i++) {
                StringTokenizer st = new StringTokenizer(bf.readLine());
                Node ni = new Node(i);
                nodes.add(ni);
                for(int j=0; j<n; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                    if(graph[i][j] == 1) nodes.get(i).connectedNodes.add(j);
                }
            }
            ArrayList<Integer> weakNodes = new ArrayList<>();
            outer:
            for(Node node : nodes) {
                ArrayList<Integer> cn = node.connectedNodes;
                for(int i=0; i<cn.size(); i++) {
                    for(int j=i+1; j<cn.size(); j++) {
                        if(nodes.get(cn.get(i)).connectedNodes.contains(cn.get(j))) continue outer;
                    }
                }
                weakNodes.add(node.n);
            }
            String out = "";
            for(int a : weakNodes) out += a + " ";
            System.out.println(out.trim());
        }
    }
}

class Node {
    int n = 0;
    ArrayList<Integer> connectedNodes = new ArrayList<>();
    Node(int x) {
        n=x;
    }
}
