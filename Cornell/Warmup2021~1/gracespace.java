import java.io.*;
import java.util.*;

public class sophieworld {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		double a = Double.parseDouble(st.nextToken());
		double b = Double.parseDouble(st.nextToken());
		double c = Double.parseDouble(st.nextToken());
		double d = Double.parseDouble(st.nextToken());
		double t = 0.0;
		// t = ((b*-1.0) + Math.sqrt(Math.pow(b,2.0)-4.0*a*c))/2.0*a;
		// if(t.isNaN()) t = ((b*-1.0) - Math.sqrt(Math.pow(b,2.0)-4.0*a*(c-d)))/2.0*a;
		// System.out.println(String.format("%.6f", Math.pow(t,2)));
		double min=0.0, max=10000000;
		while(true) {
			t = (max+min)/2.0;
			if(a*Math.pow(t,5)+b*Math.pow(t,3)+c*t < d) min=t;
			else if(a*Math.pow(t,5)+b*Math.pow(t,3)+c*t > d) max=t;
			else break;
		}
		System.out.println(String.format("%.6f", t));
	}
}