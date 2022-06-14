import java.util.*;
import java.io.*;

public class PastPrologue {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(bf.readLine());
        while(t-->0){
            int n = Integer.parseInt(bf.readLine());
            ArrayList<String> events = new ArrayList<>();
            ArrayList<String> output = new ArrayList<>();
            ArrayList<String> d = new ArrayList<>();
            HashMap<String, ArrayList<Integer>> day= new HashMap<>();
            HashMap<String, ArrayList<Integer>> night = new HashMap<>();
            for(int i=0; i<n; i++) {
                String[] line = bf.readLine().split(",");
                if(!events.contains(line[3])) {
                    events.add(line[3]);
                    ArrayList<Integer> a = new ArrayList<>();
                    night.put(line[3], a);
                    ArrayList<Integer> b = new ArrayList<>();
                    day.put(line[3], b);
                    if(line[4].equals("false")) continue;
                    if(d.contains(line[0])) continue;
                    d.add(line[0]);
                    if(line[2].equals("Day")) {
                        day.get(line[3]).add(0);
                    } else {
                        night.get(line[3]).add(0);
                    }
                } else {
                    if(line[4].equals("false")) continue;
                    if(d.contains(line[0])) continue;
                    d.add(line[0]);
                    if(line[2].equals("Day")) {
                        if(day.containsKey(line[3]))
                            day.get(line[3]).add(0);
                    } else {
                        if(night.containsKey(line[3]))
                            night.get(line[3]).add(0);
                    }
                }
            }
            for(String e : events) {
                output.add(e + "," + day.get(e).size() + "," + night.get(e).size());
            }
            Collections.sort(output);
            System.out.println(String.join("\n", output));
        }


    }
}