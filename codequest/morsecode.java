import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class morsecode {
    public static HashMap<String, String> morse = new HashMap<>();
    public static HashMap<String, String> english = new HashMap<>();

    public static String convertToMorse(String en) {
        StringBuilder sb = new StringBuilder();
        for(String a : en.split(" ")) {
            for(int i=0; i<a.length(); i++) {
                String c = a.substring(i,i+1);
                sb.append(morse.get(c)).append("   ");
            }
            sb.append("    ");
        }
        return sb.toString();
    }

    public static String convertToEnglish(String mo) {
        StringBuilder sb = new StringBuilder();
        for(String a : mo.split(" {7}")) {
            for(String b : a.split(" {3}")) {
                sb.append(english.get(b.trim()));
            }
            sb.append(" ");
        }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf= new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(bf.readLine());
        for(int k=0; k<t; k++){
            for(int i=0; i<26; i++) {
                String[] line = bf.readLine().split(" ", 2);
                morse.put(line[0], line[1]);
                english.put(line[1], line[0]);
            }
            String english = bf.readLine();
            String morse = bf.readLine();
            System.out.println(convertToMorse(english).trim());
            System.out.println(convertToEnglish(morse).trim());
        }
    }

}
