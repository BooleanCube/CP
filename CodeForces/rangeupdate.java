import java.io.*;
import java.util.*;

class Reader {
    final private int BUFFER_SIZE = 1 << 16;
    private DataInputStream din;
    private byte[] buffer;
    private int bufferPointer, bytesRead;

    public Reader()
    {
        din = new DataInputStream(System.in);
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }

    public Reader(String file_name) throws IOException
    {
        din = new DataInputStream(
            new FileInputStream(file_name));
        buffer = new byte[BUFFER_SIZE];
        bufferPointer = bytesRead = 0;
    }

    public String readLine() throws IOException
    {
        byte[] buf = new byte[64]; // line length
        int cnt = 0, c;
        while ((c = read()) != -1) {
            if (c == '\n') {
                if (cnt != 0) {
                    break;
                }
                else {
                    continue;
                }
            }
            buf[cnt++] = (byte)c;
        }
        return new String(buf, 0, cnt);
    }

    public int nextInt() throws IOException
    {
        int ret = 0;
        byte c = read();
        while (c <= ' ') {
            c = read();
        }
        boolean neg = (c == '-');
        if (neg)
            c = read();
        do {
            ret = ret * 10 + c - '0';
        } while ((c = read()) >= '0' && c <= '9');

        if (neg)
            return -ret;
        return ret;
    }

    public long nextLong() throws IOException
    {
        long ret = 0;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();
        do {
            ret = ret * 10 + c - '0';
        } while ((c = read()) >= '0' && c <= '9');
        if (neg)
            return -ret;
        return ret;
    }

    public double nextDouble() throws IOException
    {
        double ret = 0, div = 1;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();

        do {
            ret = ret * 10 + c - '0';
        } while ((c = read()) >= '0' && c <= '9');

        if (c == '.') {
            while ((c = read()) >= '0' && c <= '9') {
                ret += (c - '0') / (div *= 10);
            }
        }

        if (neg)
            return -ret;
        return ret;
    }

    private void fillBuffer() throws IOException
    {
        bytesRead = din.read(buffer, bufferPointer = 0,
                             BUFFER_SIZE);
        if (bytesRead == -1)
            buffer[0] = -1;
    }

    private byte read() throws IOException
    {
        if (bufferPointer == bytesRead)
            fillBuffer();
        return buffer[bufferPointer++];
    }

    public void close() throws IOException
    {
        if (din == null)
            return;
        din.close();
    }
}

public class rangeupdate {
	
	static void update(long[] tree, int l, int r, long u) {
		if(l == r) {
			tree[l] += u;
			return;
		}
		if(l%2 == 1) {
			tree[l] += u;
			l++;
		}
		if(l == r) {
			tree[l] += u;
			return;
		}
		if(r%2 == 0) {
			tree[r] += u;
			r--;
		}
		update(tree, l>>1, r>>1, u);
	}
	
	static long point(long[] tree, int idx) {
		long sum = tree[idx];
		while(idx > 0) {
			idx >>= 1;
        	sum += tree[idx];
		}
		return sum;
	}
	
	public static void main(String[] args) throws IOException {
		Reader sc = new Reader();
		StringBuilder sb = new StringBuilder();
		int n = sc.nextInt();
		int q = sc.nextInt();
		long[] tree = new long[2*n];
		for(int i=n; i<2*n; i++) tree[i] = sc.nextLong();
		for(int i=0; i<q; i++) {
			int type = sc.nextInt();
			if(type == 1) {
				int a = sc.nextInt();
				int b = sc.nextInt();
				long u = sc.nextLong();
				update(tree, n+a-1, n+b-1, u);
			}
			if(type == 2) {
				int idx = sc.nextInt();
				sb.append(point(tree, n+idx-1)).append("\n");
			}
		}
		System.out.println(sb.toString());
	}
	
}
