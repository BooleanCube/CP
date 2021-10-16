//yea its pretty bad, deal with it

import java.io.*;
import java.util.*;

public class Main {
  static HashMap<String, String> dictionary = new HashMap<String, String>();
  static ArrayList<String> keys = new ArrayList<>(dictionary.keySet());

  public static void main(String[] args) throws IOException {
    init();
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(bf.readLine());
    for(int i=0; i<n; i++) {
      String text = bf.readLine();
      for(int j=0; j<text.length(); j++) {
        String pre = text.substring(0, j);
        String sub = text.substring(j);
        boolean upper = containsUpper(sub);
        sub = sub.toLowerCase();
        for(String key : keys) {
          if(sub.startsWith(key)) {
            sub = dictionary.get(key) + sub.substring(key.length());
            if(upper) sub = Character.toUpperCase(sub.charAt(0)) + sub.substring(1);
            text = pre + sub;
            break;
          }
        }
      }
      System.out.println(text);
    }
  }

  public static boolean containsUpper(String str) {
    for(char c : str.toCharArray()) if(Character.isUpperCase(c)) return true;
    return false;
  }

  public static void init() {
    dictionary.put("at", "@");
    dictionary.put("and", "&");
    dictionary.put("one", "1");
    dictionary.put("won", "1");
    dictionary.put("to", "2");
    dictionary.put("too", "2");
    dictionary.put("two", "2");
    dictionary.put("for", "4");
    dictionary.put("four", "4");
    dictionary.put("bea", "b");
    dictionary.put("bee", "b");
    dictionary.put("be", "b");
    dictionary.put("sea", "c");
    dictionary.put("see", "c");
    dictionary.put("eye", "i");
    dictionary.put("oh", "o");
    dictionary.put("owe", "o");
    dictionary.put("are", "r");
    dictionary.put("you", "u");
    dictionary.put("why", "y");

    keys.add("four");
    keys.add("you");
    keys.add("won");
    keys.add("why");
    keys.add("two");
    keys.add("too");
    keys.add("see");
    keys.add("sea");
    keys.add("owe");
    keys.add("one");
    keys.add("for");
    keys.add("eye");
    keys.add("bee");
    keys.add("bea");
    keys.add("are");
    keys.add("and");
    keys.add("to");
    keys.add("oh");
    keys.add("be");
    keys.add("at");
  }
}
