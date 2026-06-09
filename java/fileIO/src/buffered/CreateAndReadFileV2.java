package buffered;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

import static buffered.BufferedConst.*;

// V2 : 버퍼 배열을 직접 만들어 구현
public class CreateAndReadFileV2 {
    public static void main(String[] args) {
        FileOutputStream fos = null;
        FileInputStream fis = null;

        try {
            fos = new FileOutputStream(FILE_NAME);
            fis = new FileInputStream(FILE_NAME);

            // 파일 쓰기 시간 측정
            System.out.println("=========================================");
            System.out.println("버퍼를 활용하여 파일 쓰기");
            long startTime1 = System.currentTimeMillis();

            // 운영체제에서 파일을 한 번에 쓰고 읽는 최대 크기가 8KB 이기에 그 이상으로 버퍼 사이즈를 키워도 변화 x
            byte[] buffer = new byte[BUFFER_SIZE]; // 한 번에 여러 바이트 데이터를 담는 배열
            int bufferIndex = 0;

            for (int i = 0; i < FILE_SIZE; i++) { // 10 * 1024 * 1024 번 반복 쓰기
                buffer[bufferIndex] = 1;
                bufferIndex++;

                if (bufferIndex == BUFFER_SIZE) { // 버퍼 배열이 가득 차면 파일에 쓰기
                    fos.write(buffer);
                    bufferIndex = 0; // 버퍼를 비운다.
                }
            }

            // 마지막에 버퍼가 다 차지 않아서 flush 되지 않을 경우
            if (bufferIndex > 0) fos.write(buffer, 0, bufferIndex); // 0부터 bufferIDX 까지 쓰기

            long endTime1 = System.currentTimeMillis();
            System.out.println("파일 쓰기 시간 : " + (endTime1 - startTime1) + " ms");
            // 버퍼를 활용한 쓰기 시간 30ms = 0.03초

            System.out.println("=========================================");

            // 파일 읽기 시간 측정
            System.out.println("버퍼를 활용하여 파일 읽기");
            long startTime2 = System.currentTimeMillis();

            byte[] buffer2 = new byte[BUFFER_SIZE];

            int size;

            boolean flag = true;
            while (flag) {
                size = fis.read(buffer2); // 버퍼 크기만큼 읽는다.
                if (size == -1) {
                    flag = false; // EoF일 때 flag를 false로 바꾸어 종료
                }
            }

            long endTime2 = System.currentTimeMillis();
            System.out.println("버퍼를 활용하여 읽기 시간 : " + (endTime2 - startTime2) + " ms");
            // 읽기 시간 2 ms = 0.002  초

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (fos != null) fos.close();
                if (fis != null) fis.close();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}

