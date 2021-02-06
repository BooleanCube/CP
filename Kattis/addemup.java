import java.io.*;
import java.util.*;
public class addemup {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n = Integer.parseInt(st.nextToken());
        int goal = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        ArrayList<Integer[]> nums = new ArrayList<>();
        for(int i=0; i<n; i++) {
            String d = st.nextToken();
            Integer[] b = new Integer[]{Integer.parseInt(d), reverse(d)};
            nums.add(b);
        }
        boolean flag = true;
        outer:
        for(int i=0; i<nums.size(); i++) {
            for(int j=i+1; j<nums.size(); j++) {
                if(nums.get(i)[0] + nums.get(j)[0] == goal) {
                    System.out.println("YES");
                    flag = false;
                    break outer;
                }
                if(nums.get(i)[0] + nums.get(j)[1] == goal) {
                    System.out.println("YES");
                    flag = false;
                    break outer;
                }
		        if(nums.get(i)[1] + nums.get(j)[0] == goal) {
                    System.out.println("YES");
                    flag = false;
                    break outer;
                }
		        if(nums.get(i)[1] + nums.get(j)[1] == goal) {
                    System.out.println("YES");
                    flag = false;
                    break outer;
                }
	        }
        }
        if(flag) System.out.println("NO");
    }
    static int reverse(String num) {
        List<Character> reversible = Arrays.asList(new Character[]{'1', '2', '5', '8', '0'});
        for(char c : num.toCharArray()) {
            if(!reversible.contains(c))  return Integer.MIN_VALUE;
        }
        return Integer.parseInt(new StringBuilder(num).reverse().toString());
    }
}
