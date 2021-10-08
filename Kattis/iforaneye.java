import java.io.*;
import java.util.*;

public class iforaneye {
    public HashMap<String, String> dictionary = new HashMap<>();
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String[] keys = dictionary.keySet().toArray();
        int n = Integer.parseInt(bf.readLine());
        for(int i=0; i<n; i++) {
            String in = bf.readLine();
            for(String s : keys) {
                if(in.indexOf("-" + s + "-") != in.indexOf(s)-1) in.replaceFirst(s, "-" + dictionary.get(s) + "-");
            }
        }
    }

    public void initializeDictionary() {
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
    }
}
