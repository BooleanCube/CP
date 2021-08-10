import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int c = Integer.parseInt(bf.readLine());
		for(int i=0; i<c; i++) {
			int n = Integer.parseInt(bf.readLine());
			PriorityQueue<Stock> stocks = new PriorityQueue<>();
			long net = 0;
			for(int j=0; j<n; j++) {
				StringTokenizer st = new StringTokenizer(bf.readLine());
				String query = st.nextToken();
				int share = Integer.parseInt(st.nextToken());
				long price = Long.parseLong(st.nextToken());
				
				
				if(query.equalsIgnoreCase("BUY")) {
					Stock stock = new Stock(share, price);
					stocks.offer(stock);
				} else {
					while(share > 0) {
						Stock s = stocks.poll();
						if(share >= s.shares) {
							net += (-s.price*s.shares + price*s.shares);
							share -= s.shares;
						} else {
							net += (-s.price*share + price*share);
							s.shares -= share;
							share = 0;
							stocks.offer(s);
						}
					}
				}
			}
			System.out.println(net);
		}
	}
}

class Stock implements Comparable<Stock> {
	
	int shares;
	long price;
	
	public Stock(int s, long p) {
		shares = s;
		price = p;
	}

	@Override
	public int compareTo(Stock s) {
		return -Long.compare(price, s.price);
	}

}