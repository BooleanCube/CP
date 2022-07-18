import java.io.*;
import java.util.*;

public class strmin {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(bf.readLine());
		while(t-- > 0) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			char[] s = new char[m]; for(int i=0; i<m; i++) s[i] = 'B';
			st = new StringTokenizer(bf.readLine());
			for(int i=0; i<n; i++) {
				int op = Integer.parseInt(st.nextToken());
				int so = m+1-op;
				op--;
				so--;
				if(op < so) {
					if(s[op] == 'A') s[so] = 'A';
					else s[op] = 'A';
				} else {
					if(s[so] == 'A') s[op] = 'A';
					else s[so] = 'A';
				}
			}
			StringBuilder sb = new StringBuilder();
			for(char c : s) sb.append(c);
			System.out.println(sb.toString());
		}
	}

}
