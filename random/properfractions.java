import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class properfractions {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BigInteger n = new BigInteger(bf.readLine());
        long l = n.longValue();
        for(BigInteger i=new BigInteger("1"); i.longValue()<l; i=i.add(new BigInteger("1")))
            if(i.gcd(n).longValue() == 1) System.out.println(i.longValue() + "/" + l);
    }
}
