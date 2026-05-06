
import java.util.*;
import java.io.*;
class Greedy1 {
	static int N;
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		List<Member> members = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			String[] input = br.readLine().split(" ");
			members.add(new Member(Integer.parseInt(input[0]), Integer.parseInt(input[1])));
		}

		Collections.sort(members, (m1, m2) -> {
			if (m1.height == m2.height) return m2.weight - m1.weight; // 내림차순
			else return m2.height - m1.height;
		});
		
		int answer = 0;
		for (int i = 0; i < N - 1; i++) {
			if (members.get(i).height > members.get(i + 1).height 
				&& members.get(i).weight > members.get(i + 1).weight 
			) answer++;
		}
		System.out.println(N - answer);
		
	}
	static class Member {
		int height;
		int weight;
		Member (int height, int weight) {
			this.height = height;
			this.weight = weight;
		}
	}

}
