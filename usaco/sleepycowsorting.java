// 3/12 test cases lmao
import java.io.*;
import java.util.*;

public class sleepycowsorting {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new FileReader(new File("sleepy.in")));
        FileWriter fw = new FileWriter("sleepy.out");
        int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int steps = 0;
        ArrayList<Integer> cows = new ArrayList<>();
        for(int i=0; i<n; i++) {
            cows.add(Integer.parseInt(st.nextToken()));
        }
        int num = n;
        while(true) {
            int idx = cows.indexOf(num);
            if(idx == -1) break;
            if(idx == num-1 || idx == 0) { --num; continue; }
            else {
                if(cows.get(0) == 1) cows.add(idx, cows.remove(0));
                else cows.add(cows.indexOf(cows.get(0)-1), cows.remove(0));
                num = n;
                ++steps;
            }
        }
        fw.write(String.valueOf(steps));
        fw.flush(); fw.close();
    }
}
