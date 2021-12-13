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

    //I pressed enter for the first time in my life
	static int getScore(String[][] board, int call) {
		int sum = 0;
		for(int i=0; i<board.length; i++) {
			for(int j=0; j<board[i].length; j++) {
				if(board[i][j] != null) sum += Integer.parseInt(board[i][j]);
			}
		}
		return sum * call;
	}
	static void clearCalls(String[][] board, String call) {
		for(int i=0; i<board.length; i++) {
			for(int j=0; j<board[i].length; j++) {
				if(board[i][j] != null && board[i][j].equals(call)) board[i][j] = null;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String callNums = bf.readLine();
		String[][][] boards = new String[100][5][5];
		for(int i=0; i<100; i++) {
			bf.readLine();
			for(int j=0; j<5; j++) boards[i][j] = bf.readLine().trim().split("\\s+");
		}
		StringTokenizer calls = new StringTokenizer(callNums, ",");
		outer:
		while(calls.hasMoreTokens()) {
			String call = calls.nextToken();
			for(int i=0; i<boards.length; i++) {
				clearCalls(boards[i], call);
				if(checkWin(boards[i])) {
					System.out.println(getScore(boards[i], Integer.parseInt(call)));
					break outer;
				}
			}
		}
	}

}
