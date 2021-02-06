import java.io.*;
import java.util.*;

public class zagrade {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String e = bf.readLine();
        HashMap<Integer, Integer> ind = new HashMap<>();
        Deque<Integer> pairs = new ArrayDeque<>();
        ArrayList<Integer> keys = new ArrayList<>();
        for(int i=0; i<e.length(); i++) {
            char c = e.charAt(i);
            if(c=='(') pairs.addLast(i);
            if(c==')') { int p = pairs.removeLast(); ind.put(p, i); keys.add(p); }
        }
        int n = (int)(Math.pow(2, keys.size())-1)-1;
        int s = keys.size();
        ArrayList<String> p = new ArrayList<>();
        while(n>=0) {
            String bin = fix(Integer.toBinaryString(n), s);
            String c = e;
            //System.out.println(bin);
            for(int i=0; i<bin.length(); i++) if(bin.charAt(i) == '0') c = c.substring(0, keys.get(i)) + "g" + c.substring(keys.get(i)+1, ind.get(keys.get(i))) + "g" + c.substring(ind.get(keys.get(i))+1);
            if(!p.contains(c.replaceAll("g", ""))) p.add(c.replaceAll("g", ""));
            n--;
        }
        Collections.sort(p);
        for(String lk : p) System.out.println(lk);
    }
    static String fix(String b, int n) {
        int s = n-b.length();
        if(s==0) return b;
        String res = "";
        for(int i=0; i<s; i++) res+="0";
        //System.out.println(res+b);
        return res+b;
    }
}
