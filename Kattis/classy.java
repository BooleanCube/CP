import java.io.*;
import java.util.*;

public class classy {
    public static void main(String[] args)throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Double, String> map = new HashMap<>();
        ArrayList<Double> scores = new ArrayList<>();
        int t = Integer.parseInt(bf.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(bf.readLine());
            while(n-- > 0) {
                String in = bf.readLine();
                String name = in.split(": ")[0];
                String[] rank = in.replaceAll(" class", "").split(": ")[1].split("-");
                double score = 0;
                if(rank[rank.length-1].equals("upper")) score+=3.0;
                if(rank[rank.length-1].equals("middle")) score+=2.0;
                if(rank[rank.length-1].equals("lower")) score+=1.0;
                double b = score+1.0;
                for(int j=rank.length-2; j>=0; j--) {
                    if(rank[j].equals("lower")) score+=(b-score)*0.25;
                    if(rank[j].equals("middle")) score+=(b-score)*0.50;
                    if(rank[j].equals("upper")) score+=(b-score)*0.75;
                }
                map.put(score, name);
                scores.add(score);
            }
            Collections.sort(scores);
            Collections.reverse(scores);
            for(double d:scores) System.out.println(map.get(d));
            System.out.println("==============================");
        }
    }
}
