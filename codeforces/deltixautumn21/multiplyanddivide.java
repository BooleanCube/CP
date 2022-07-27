import java.io.*;
import java.util.*;

public class multiplyanddivide {
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        while(t-- > 0) {
            int n = Integer.parseInt(bf.readLine());
            StringTokenizer st = new StringTokenizer(bf.readLine());
            ArrayList<Integer> arr = new ArrayList<>();
            while(st.hasMoreTokens()) arr.add(Integer.parseInt(st.nextToken()));
            long prevSum = 0;
            long currentSum = arr.stream().mapToLong(Integer::longValue).sum();
            while(prevSum < currentSum) {
                prevSum = currentSum;
                int idxMin = idxOfLowestEven(arr);
                int idxMax = arr.indexOf(Collections.max(arr));
                if(idxMin < 0) break;
                if(idxMin == idxMax) {
                    int dupMin = idxOfFirstDup(arr, idxMin);
                    if(dupMin < 0) {
                        int dupMax = idxOfFirstDup(arr, idxMax);
                        if(dupMax < 0) break;
                        else idxMax = dupMax;
                    } else idxMin = dupMin;
                }
                arr.add(idxMin, arr.remove(idxMin)/2);
                arr.add(idxMax, arr.remove(idxMax)*2);
                currentSum = arr.stream().mapToLong(Integer::longValue).sum();
            }
            System.out.println(prevSum);
        }
    }

    static int idxOfLowestEven(ArrayList<Integer> arr) {
        int idx = -1;
        int min = 16;
        for(int i=0; i<arr.size(); i++) {
            if(arr.get(i) < min && arr.get(i) % 2 == 0) {
                min = arr.get(i);
                idx = i;
            }
        }
        return idx;
    }

    static int idxOfFirstDup(ArrayList<Integer> arr, int idx) {
        for(int i=0; i<arr.size(); i++) {
            if(i==idx) continue;
            if(arr.get(i) == arr.get(idx)) return i;
        }
        return -1;
    }

}
