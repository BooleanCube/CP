import java.io.*;
import java.util.*;

public class kyokorythm {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		String r = bf.readLine();
		int co = 0;
		int score = 0;
		for(int i=0; i<n; i++) {
			char c = r.charAt(i);
			if(c == '*') {score+=100;score+=co;++co;}
			else if(c == 'o') {score+=100;score+=co;++co;}
			else co=0;
		}
		System.out.println(score);
	}
}