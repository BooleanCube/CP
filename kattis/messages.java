import java.io.*;
import java.util.*;

public class messages {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int end = 0;
        ArrayList<String> dictionary = new ArrayList<>();
        StringBuilder word = new StringBuilder();
        while(true) {
            if(end == 0) {
                String in = bf.readLine();
                if(in.equals("#")) { 
                    ++end;
                    Collections.sort(dictionary, new Comparator<String>() {
                        public int compare(String a, String b) {
                            if(Integer.compare(a.length(),b.length()) == 0) {
                                return a.compareTo(b);
                            } else return Integer.compare(a.length(),b.length());
                        }
                    });
                }
                else dictionary.add(in);
            }
            if(end == 1) {
                String c = bf.readLine();
                if(c.equals("#")) break;
                for(int i=0; i<c.length(); i++) {
                    if(c.substring(i, i+1).equals("|")) {
                        String d = word.toString();
                        int count = 0;
                        for(int j=0; j<d.length();) {
                        	String o = d;
                        	for(String key : dictionary) {
                        		if(d.startsWith(key)) {
                        			++count;
                        			d = d.substring(key.length());
                        			break;
                        		}
                        	}
                        	if(o.equals(d)) d = d.substring(1);
                        }
                        word = new StringBuilder();
                        System.out.println(count);
                    } else word.append(c.substring(i, i+1));
                }
            }
        }
    }
}
