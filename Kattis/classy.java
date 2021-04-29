//TLE

import java.io.*;
import java.util.*;

public class classy {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Double, ArrayList<String>> scoreMap = new HashMap<>();
        ArrayList<Double> scores = new ArrayList<>();
        int t = Integer.parseInt(bf.readLine());
        for(int i=0; i<t; i++) {
            int n = Integer.parseInt(bf.readLine());
            String[] classes = new String[n];
            String[] names = new String[n];
            int maxLen = 0;
            for(int j=0; j<n; j++) {
                String[] in = bf.readLine().split(": ");
                String name = in[0]; String clas = in[1].replaceAll(" class", "");
                names[j] = name;
                classes[j] = clas;
                if(clas.split("-").length > maxLen) maxLen = clas.split("-").length;
            }
            ArrayList<String> classList = fixClassLength(classes, maxLen);
            int a=0;
            for(String s : classList) {
                double score = calculateScore(s);
                ArrayList<String> st = new ArrayList<>();
                st.add(names[a]);
                if(scoreMap.containsKey(score)) scoreMap.get(score).add(names[a]);
                else scoreMap.put(score, st);
                if(!scores.contains(score)) scores.add(score);
                ++a;
            }
            Collections.sort(scores);
            for(int j=scores.size()-1; j>=0; --j) {
                Collections.sort(scoreMap.get(scores.get(j)));
                for(int k=0; k<scoreMap.get(scores.get(j)).size(); k++) System.out.println(scoreMap.get(scores.get(j)).get(k));
            }
            System.out.println("==============================");
            scores.clear();
            scoreMap.clear();
        }
    }
    static ArrayList<String> fixClassLength(String[] c, int max) {
        ArrayList<String> ret = new ArrayList<>();
        for(String s : c) {
            String[] l = s.split("-");
            String ac = s;
            if(l.length < max) for(int i=0; i<max-l.length; i++) ac="middle-"+ac;
            ret.add(ac);
        }
        return ret;
    }
    static double calculateScore(String classes) {
        double score = 0;
        double b = 4;
        String[] l = classes.split("-");
        switch(l[0]) {
            case "upper": 
                score+=3;
                break;
            case "middle": 
                score+=2; b-=1;
                break;
            case "lower": 
                score+=1; b-=2;
                break;
        }
        for(int i=1; i<l.length; i++) {
            switch(l[i]) {
                case "upper":
                    score += (b-score)*0.75;
                    break;
                case "middle":
                    score += (b-score)*0.50;
                    break;
                case "lower": 
                    score += (b-score)*0.25;
            }
        }
        return score;
    }
}
