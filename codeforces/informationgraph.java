import java.io.*;
import java.util.*;

public class informationgraph {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int total = Integer.parseInt(st.nextToken());
        int events = Integer.parseInt(st.nextToken());
        int doc = 0;
        StringBuilder sb = new StringBuilder();
        employee[] tree = new employee[total];
        for(int i=0; i<total; i++) tree[i] = new employee(i+1);
        for(int i=0; i<events; i++) {
            st = new StringTokenizer(bf.readLine());
            int type = Integer.parseInt(st.nextToken());
            if(type == 1) {
                int emp = Integer.parseInt(st.nextToken());
                int boss = Integer.parseInt(st.nextToken());
                tree[emp-1].boss = tree[boss-1];
            } else if(type == 2) {
                ++doc;
                int start = Integer.parseInt(st.nextToken());
                employee current = tree[start-1];
                while(current.boss != null) {
                    current.documents.add(doc);
                    current = current.boss;
                }
                current.documents.add(doc);
            } else if(type == 3) {
                int employee = Integer.parseInt(st.nextToken());
                int document = Integer.parseInt(st.nextToken());
                sb.append(tree[employee-1].documents.contains(document) ? "YES\n" : "NO\n");
            }
        }
        System.out.println(sb.toString());
    }
}

class employee {
    public HashSet<Integer> documents = new HashSet<>();
    public int num = -1;
    public employee boss;

    public employee(int num) {
        this.num = num;
    }
}
