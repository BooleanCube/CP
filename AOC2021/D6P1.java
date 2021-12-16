import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine(), ",");
		ArrayList<Integer> fishies = new ArrayList<>();
		while(st.hasMoreTokens()) fishies.add(Integer.parseInt(st.nextToken()));
		for(int i=0; i<80; i++) {
			int countOnes = 0;
			for(int j=0; j<fishies.size(); i++) {
				if(fishies.get(j) == 1) countOnes++;
				fishies.add(j, fishies.remove(j));
			}
			while(countOnes-- > 0) fishies.add(8);
      System.out.println(fishies);
		}
		System.out.println(fishies.size());
	}

}
