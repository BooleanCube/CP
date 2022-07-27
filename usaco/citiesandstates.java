import java.io.*;
import java.util.*;

public class citiesandstates {
    public static void main(String[] args) throws IOException {
        HashMap<String, String> map = new HashMap<>();
        File in = new File("citystate.in");
        BufferedReader bf = new BufferedReader(new FileReader(in));
        int n = Integer.parseInt(bf.readLine());
        int counter = 0;
        for(int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            String city = st.nextToken().substring(0, 2);
            String state = st.nextToken();
            map.put(city, state);
            if(map.containsKey(state) && map.get(state).equals(city)) ++counter;
        }
        FileWriter fw = new FileWriter(new File("citystate.out"));
        fw.write(counter);
        fw.flush();
    }
}
