//i attempted the problem in c++, to practice my c++ skillz so go check that one instead.
import java.util.*;
import java.io.*;

public class binarytree {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(bf.readLine());
		while(n-- > 0) {
			String s = bf.readLine();
			String t = bf.readLine();
			
		}
	}
}

class tree {
	public node root = new node();
	public tree() {root.parent = root;}
}

class node {
	public node left = null;
	public node right = null;
	public node parent = null;
}
