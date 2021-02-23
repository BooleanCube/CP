import java.io.*;
import java.util.*;

public class alphabet {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String str = bf.readLine();
		int counter = 0;
		for(int i=1; i<str.length(); i++) {
			int x = (int)str.charAt(i-1);
			int y = (int)str.charAt(i);
			if(y<x) {
				int c1=0;
				int c2=0;
				for(int j=i+1; j<str.length(); j++) {
					if(x<(int)str.charAt(j)) c1++;
					if(y<(int)str.charAt(j)) c2++;
				}
				if(c2>c1) str = str.substring(0, i-1) + str.substring(i);
				else str = str.substring(0, i) + str.substring(i+1);
				i=0;
				counter++;
			}
		}
		System.out.println();
		System.out.println(str);
		System.out.println(counter);
	}
}