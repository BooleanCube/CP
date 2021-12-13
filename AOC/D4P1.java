import java.util.*;
import java.io.*;

public class Main {

	static boolean checkWin(String[][] board) {
		for(int i=0; i<board.length; i++) {
			int iCount = 0;
			int jCount = 0;
			for(int j=0; j<board[i].length; j++) {
				if(board[i][j] == null) ++iCount;
				if(board[j][i] == null) ++jCount;
			}
			if(iCount >= 5 || jCount >= 5) return true;
		}
		return false;
	}

	static getScore(String[][] board) {

	}

	public static void main(String[] args) {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String callNums = bf.readLine();
		String[][][] boards = new String[][][];
		for(int i=0; i<100; i++) {
			bf.readLine();
			for(int j=0; j<5; j++) boards[i][j] = bf.readLine().split("\\s+");
		}
		StringTokenizer calls = new StringTokenizer(callNums, ",");
		while(calls.hasMoreTokens()) {

		}
	}

}
