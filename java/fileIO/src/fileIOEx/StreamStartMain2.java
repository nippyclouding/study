package fileIOEx;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class StreamStartMain2 {
    public static void main(String[] args) {
        FileOutputStream fos = null;
        FileInputStream fis = null;

        try {
            // 바이트 배열 쓰기
            fos = new FileOutputStream("temp/test2.dat");
            byte[] input = {65, 66, 67};
            fos.write(input);

            // 바이트 배열 읽기
            fis = new FileInputStream("temp/test2.dat");
            byte[] buffer = new byte[10];
            int readCount = fis.read(buffer, 0, 10); // offset 0부터 시작하여 최대 length 10개 데이터를 읽는다.

            System.out.println("readCount = " + readCount);
            System.out.println(Arrays.toString(buffer)); // byte 배열 -> String 배열


            byte[] readBytes = fis.readAllBytes(); // 바이트 배열 전체 데이터 조회
            System.out.println(Arrays.toString(readBytes));

            /*
             fis.read(buffer) 로 다른 파라미터를 전달하지 않을 경우 처음부터 배열 값이 존재하는 부분까지만 읽어 세아린다.
             fis.read(buffer, 0, 10) : 메모리 사용량 제어 가능, 일정 크기의 데이터를 반복적으로 읽을 때 유용하다.
             대용량 파일을 처리할 때 readAllBytes로 한 번에 메모리에 로드하기 보다 0, 10 (offset, length 파라미터)을 사용하여 나누어 읽으면 성능적으로 유리하다.

             readAllBytes - 한 번의 호출로 모든 데이터를 읽을 수 있지만 메모리 사용량을 제어할 수 없기에
             큰 파일의 경우 OutOfMemoryError가 발생할 수 있다. => 작은 파일이나 메모리에 모든 내용을 올려 처리하는 경우 적합
             */

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (fos != null) {
                    fos.close();
                }
                if (fis != null) {
                    fis.close();
                }
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
