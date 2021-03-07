//NOT WORKING
import java.io.*;
import java.util.*;

public class alphabetanimals {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<String> animals = new ArrayList<>();
        ArrayList<String> unvisited = new ArrayList<>();
        String f = bf.readLine();
        animals.add(f);
        int n = Integer.parseInt(bf.readLine());
        String output = "?";
        boolean cube = true;
        for(int i=0; i<n; i++) {
            String animal = bf.readLine();
            animals.add(animal);
            unvisited.add(animal);
        }
        String word = f;
        while(true) {
            String current = "";
            if((current=nextAnimal(unvisited, word)) != null) {
                unvisited.remove(current);
                animals.remove(current);
                if(nextAnimal(animals, current) == null) { output=current+"!"; break; }
                else if(cube && nextAnimal(animals, current) != null) { output=current; cube = false; word = f; }
                animals.add(current);
            } else break;
        }
        System.out.println(output);
    }

    static String nextAnimal(ArrayList<String> animals, String a) {
        String c = a.substring(a.length()-1);
        for(String as : animals) {
            if(as.startsWith(c)) return as;
        }
        return null;
    }
}
