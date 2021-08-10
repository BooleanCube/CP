import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bf.readLine());
		for(int i=0; i<t; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			String s = st.nextToken(); int n = s.length();
			double x = Double.parseDouble(st.nextToken());
			double y = Double.parseDouble(st.nextToken());
			int distance = (int) Math.floor(Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)));
			System.out.println(s.charAt(distance%n));
		}
	}
}