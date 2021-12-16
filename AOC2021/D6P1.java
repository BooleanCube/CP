import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine(), ",");
		ArrayList<Integer> fishies = new ArrayList<>();
		while(st.hasMoreTokens()) fishies.add(Integer.parseInt(st.nextToken()));
		for(int i=0; i<256; i++) {
			int countOnes = 0;
			for(int j=0; j<fishies.size(); j++) {
				if(fishies.get(j) == 0) {
					fishies.add(j, fishies.remove(j)+6);
					countOnes++;
				}
				else fishies.add(j, fishies.remove(j)-1);
			}
			while(countOnes-- > 0) fishies.add(8);
      			System.out.println(i);
			System.out.println(fishies.size());
		}
		System.out.println(fishies.size());
	}

}
