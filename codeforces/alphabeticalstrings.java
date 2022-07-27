import java.io.*;
import java.util.*;

public class alphabeticalstrings {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        int t = Integer.parseInt(bf.readLine());
        for(int i=0; i<t; i++) {
            String word = bf.readLine();
            String current = "";
            int idx = 0;
            boolean cube = true;
            if(word.charAt(0) > word.charAt(word.length()-1)) {current = String.valueOf(word.charAt(0));idx=0;}
            else {current = String.valueOf(word.charAt(word.length()-1));idx=word.length()-1;}
            while(!word.equals("a")) {
                if(word.length()==1) {cube = false; break;} 
                if(idx==0) word = word.substring(1);
                else word = word.substring(0, word.length()-1);
                if(!current.equals("a")) current = String.valueOf(alphabet.charAt(alphabet.indexOf(current)-1));
                else { cube=false; break; }
                idx = word.indexOf(current);
                if(!(idx == 0 || idx == word.length()-1)) { cube = false; break; }
            }
            if(cube) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}
