import java.io.*;
import java.util.*;

public class heat {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int c = Integer.parseInt(bf.readLine());
		for(int i=0; i<c; i++) {
			StringTokenizer st = new StringTokenizer(bf.readLine());
			int n = Integer.parseInt(st.nextToken());
			String d = st.nextToken();
			int t = 1;
			if(d.equalsIgnoreCase("E")) t = -1;
			ArrayList<City> cities = new ArrayList<>();
			for(int j=0; j<n; j++) {
				st = new StringTokenizer(bf.readLine());
				City city = new City(st.nextToken(), t*Double.parseDouble(st.nextToken()));
				cities.add(city);
			}
			
			Collections.sort(cities, new Comparator<City>() {
				public int compare(City o, City t) {
					if(o.lon == t.lon) {
						return o.name.compareTo(t.name);
					}
					return Double.compare(o.lon, t.lon);
				}
			});
			
			for(int j=0; j<n; j++) {
				System.out.println(cities.get(j).name);
			}
		}
	}
}

class City {
	String name;
	double lon;
	
	public City(String s, double d) {
		name = s;
		lon = d;
	}
}