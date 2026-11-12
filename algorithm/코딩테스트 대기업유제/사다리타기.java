import java.util.*;

// 메인 클래스
public class 사다리타기 {

    public static void main(String[] args) {

        // 테스트 케이스 실행
        runTest(
                5,
                new int[][]{
                        {1, 3},
                        {2, 4},
                        {1, 4}
                },
                new char[]{'D', 'B', 'A', 'C', 'E'}
        );

        runTest(
                7,
                new int[][]{
                        {1, 3, 5},
                        {1, 3, 6},
                        {2, 4}
                },
                new char[]{'A', 'C', 'B', 'F', 'D', 'G', 'E'}
        );

        runTest(
                8,
                new int[][]{
                        {1, 5},
                        {2, 4, 7},
                        {1, 5, 7},
                        {2, 5, 7}
                },
                new char[]{'C', 'A', 'B', 'F', 'D', 'E', 'H', 'G'}
        );

        runTest(
                12,
                new int[][]{
                        {1, 5, 8, 10},
                        {2, 4, 7},
                        {1, 5, 7, 9, 11},
                        {2, 5, 7, 10},
                        {3, 6, 8, 11}
                },
                new char[]{'C', 'A', 'F', 'B', 'D', 'I', 'E', 'K','G', 'L', 'J', 'H'}
        );
    }

    // 테스트 실행 함수
    static void runTest(int n, int[][] ladder, char[] expected) {

        char[] result = solution(n, ladder);

        System.out.println("=================================");
        System.out.println("n = " + n);

        System.out.println("result   = " + Arrays.toString(result));
        System.out.println("expected = " + Arrays.toString(expected));

        boolean same = Arrays.equals(result, expected);

        System.out.println("PASS = " + same);
        System.out.println("=================================\n");
    }

    // 실제 알고리즘 구현 위치
    static char[] solution(int n, int[][] ladder) {

        /*
         * TODO:
         * 실제 사다리 알고리즘 구현
         */
	// 배열 초기화 
	char[] init = new char[n];
	for (int i = 0; i < n; i++) {
		init[i] = (char) ('A' + i);
	}	

	for (int [] arr : ladder) {
		for (int i = 0; i < arr.length; i++) {
			swap(init, arr[i]);
		}
	}

        return init;
    }
	static void swap(char[] arr, int idx) {
		char temp = arr[idx - 1];
		arr[idx - 1] = arr[idx];
		arr[idx] = temp; 	
	}
}
