import java.io.*;
import java.util.*;

public class coinstacks {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        ArrayList<Integer> stacks = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(bf.readLine());
        for(int i=0; i<n; i++) stacks.add(Integer.parseInt(st.nextToken()));
        boolean flag = true;
        String steps = "";
        while(countNonEmpty(stacks) > 0) {
            if(countNonEmpty(stacks) == 1) { flag = false; break; }
            int min = 0; int minVal = Integer.MAX_VALUE;
            int max = 0; int maxVal = Integer.MIN_VALUE;
            for(int i=0; i<n; i++) {
                if(stacks.get(i) > 0 && stacks.get(i) > maxVal) { max = i; maxVal = stacks.get(i); }
                if(stacks.get(i) > 0 && stacks.get(i) < minVal) { min = i; minVal = stacks.get(i); }
            }
            if(min == max) max = stacks.lastIndexOf(maxVal);
            steps += (min+1) + " " + (max+1) + "\n";
            stacks.add(min, stacks.remove(min) - 1);
            stacks.add(max, stacks.remove(max) - 1);
        }
        if(flag) System.out.print("yes\n" + steps);
        else System.out.println("no");
    }

    public static int countNonEmpty(ArrayList<Integer> stacks) {
        int counter = 0;
        for(int a : stacks) if(a > 0) counter++;
        return counter;
    }
}
