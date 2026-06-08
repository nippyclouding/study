
import java.util.*;
import java.io.*;
class Recursive3 {
	static int N;
	public static void main(String[] arg) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		System.out.println(solution(N));
	}
	private static Long solution(int num) {
		if (num == 1) return (long) num; 
		else {
			return solution(num - 1) * num;
		}
	}

}
