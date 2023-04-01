import java.io.*;
import java.util.*;

public class wordladder {
    public static int dists[][]; 
    public static char words[][];

    public static void main(String[] args) throws Exception {	
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out);
        
        int n = Integer.parseInt(bf.readLine());
        dists = new int[n][n];
        words = new char[n][];
        
        for(int i=0; i<n; i++) {
            String word = bf.readLine();
            words[i] = word.toCharArray();
            for(int j=0; j<i; j++) {
                int count = 0;
                for(int k=0; k<words[i].length && count<3; k++) if(words[i][k]!=words[j][k]) ++count;
                dists[i][j] = dists[j][i] = count;
            }
        }
        
        boolean visited[][] = new boolean[2][n];
        Arrays.fill(visited[0], false);
        Arrays.fill(visited[1], false);
        
        ArrayDeque<State> pq = new ArrayDeque<State>();
        pq.addLast(new State(0, 0, null, "0"));
        State solution = new State(-1, 1, null, "0" );
        
        while(!pq.isEmpty()) {
            State s = pq.removeFirst();
            int used = s.add.charAt(0) == '0' ? 0 : 1;
            if(visited[used][s.word]) continue;
            visited[used][s.word]= true;
            if(s.word == 1) {
                solution = s;
                break;
            }
            
            for(int i=0; i<n; i++) if(i!=s.word) {
                if(dists[i][s.word]==1) {
                    if(!visited[used][i]) pq.addLast(new State(s.distance+1, i, s, s.add));   
                }
                else if(used==0 && dists[i][s.word]==2 && !visited[1][i]) {
                    char newword[] = new char[words[i].length];
                    boolean usei = false;
                    boolean uses = false;
                    for(int k=0; k<words[i].length; k++) {
                        if(words[i][k]==words[s.word][k]) newword[k] = words[i][k];
                        else if(usei) newword[k] = words[i][k];
                        else if(uses) newword[k] = words[s.word][k];
                        else if(words[i][k]<words[s.word][k]) {
                            newword[k] = words[i][k];
                            uses = true;
                        }
                        else if(words[i][k]>words[s.word][k]) {
                            newword[k] = words[s.word][k];
                            usei = true;
                        }
                    }
                    
                    pq.addLast(new State(s.distance+2, i, s, new String(newword)));
                }
            }
        }
        
        pw.println(solution.add);
        pw.println(solution.distance);
        pw.close();
    }   
}

class State implements Comparable<State> {
    public int distance;
    public int word;
    public String add;
    public State from;

    public State(int distance, int word, State from, String add) {
        this.distance = distance;
        this.word = word;
        this.add = add;
        this.from = from;
    }

    public int compareTo(State s) {
        int diff = distance - s.distance;
        if(diff==0) diff = add.compareTo(s.add);
        return diff;
    }
}
