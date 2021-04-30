//Wrong Answer

import java.io.*;
import java.util.*;
public class virtualfriends {
  public static void main(String[] args) throws IOException {
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    HashMap<String, ArrayList<String>> friends = new HashMap<>();
    int n = Integer.parseInt(bf.readLine());
    for(int i=0; i<n; i++) {
      int t = Integer.parseInt(bf.readLine());
      for(int j=0; j<t; j++) {
        String[] names = bf.readLine().split(" ");
        if(friends.containsKey(names[0])) friends.get(names[0]).add(names[1]);
        else { ArrayList<String> f = new ArrayList<>(); f.add(names[1]); friends.put(names[0], f); }
        if(friends.containsKey(names[1])) friends.get(names[1]).add(names[0]);
        else { ArrayList<String> f = new ArrayList<>(); f.add(names[0]); friends.put(names[1], f); }
        HashSet<String> f = new HashSet<>();
        friends.get(names[0]).forEach(fr -> { f.add(fr); });
        friends.get(names[1]).forEach(fr -> { f.add(fr); });
        System.out.println(f.size());
        f.forEach(fr -> {
            if(!friends.get(names[0]).contains(fr) && !names[0].equals(fr)) friends.get(names[0]).add(fr);
            if(!friends.get(names[1]).contains(fr) && !names[1].equals(fr)) friends.get(names[1]).add(fr);
        });
        friends.forEach(k, v -> {
            if(!v.contains(names[0]))
        });
        System.out.println(names[0] + ": " + friends.get(names[0]));
        System.out.println(names[1] + ": " + friends.get(names[1]));
      }
    }
  }
}
