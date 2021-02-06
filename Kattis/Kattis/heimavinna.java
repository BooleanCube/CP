import java.util.*;
import java.io.*;


public class heimavinna {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String in = bf.readLine();
        String[] nums = in.split(";");
        ArrayList<Integer> l = new ArrayList<>();
        for(String num : nums) {
            if(num.indexOf("-") > -1) {
                String[] ind = num.split("-");
                int start = Integer.parseInt(ind[0]);
                int end = Integer.parseInt(ind[1]);
                for(int i=start; i<=end; i++) l.add(i);
            } else l.add(Integer.parseInt(num));
        }
        System.out.println(l.size());
    }
}
