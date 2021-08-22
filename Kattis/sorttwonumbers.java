// This was a joke, please don't assasinate me
// https://en.wikipedia.org/wiki/Bogosort

import java.io.*;
import java.util.*;

public class sorttwonumbers {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> nums = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(bf.readLine());
        while(st.hasMoreTokens()) nums.add(Integer.parseInt(st.nextToken()));
        ArrayList<Integer> sorted = bogo(nums);
        for(int a : sorted) System.out.print(a + " ");
    }

    static ArrayList<Integer> bogo(ArrayList<Integer> nums) {
        while(true) {
            if(isSorted(nums)) break;
            Collections.shuffle(nums);
        }
        return nums;
    }

    static boolean isSorted(ArrayList<Integer> nums) {
        int prev = -1;
        for(int a:nums) {
            if(a<prev) return false;
            prev = a;
        }
        return true;
    }

}
