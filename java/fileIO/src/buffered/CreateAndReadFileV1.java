package buffered;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

import static buffered.BufferedConst.FILE_NAME;
import static buffered.BufferedConst.FILE_SIZE;

// V1 : 버퍼 없이 직접 파일 크기만큼 1byte싹 반복해서 읽고 쓰기
public class CreateAndReadFileV1 {
    public static void main(String[] args) {
        FileOutputStream fos = null;
        FileInputStream fis = null;


        try {
            fos = new FileOutputStream(FILE_NAME);
            fis = new FileInputStream(FILE_NAME);

            // 파일 쓰기 시간 측정
            System.out.println("=========================================");
            System.out.println("1바이트씩 10 * 1024 * 1024 번 반복해서 파일 쓰기");
            long startTime1 = System.currentTimeMillis();

            for (int i = 0; i < FILE_SIZE; i++) {
                fos.write(1); // 10 * 1024 * 1024 번 반복 쓰기
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println("파일 쓰기 시간 : " + (endTime1 - startTime1) + " ms");
            // 쓰기 시간 15706 ms = 15.7초 소요

            System.out.println("=========================================");

            // 파일 읽기 시간 측정
            System.out.println("1바이트씩 10 * 1024 * 1024 번 반복해서 파일 읽기");
            long startTime2 = System.currentTimeMillis();

            int fileSize = 0;
            int data;
            while ((data = fis.read()) != -1) {
                fileSize++; // 10 * 1024 * 1024 번 반복 읽기 (다 읽으면 -1 출력)
            }

            long endTime2 = System.currentTimeMillis();
            System.out.println("파일 읽기 시간 : " + (endTime2 - startTime2) + " ms");
            // 읽기 시간 5449 ms = 5.4초 소요

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

/*
10MB 파일 쓰기에 약 15초, 파일 읽기에 약 5초 시간 소요
Java 에서 1byte씩 디스크에 데이터를 전달하고, 또 디스크에서 데이터를 읽어오기에 많은 시간이 소요된다.

정확히는 write(), read() 호출 시 OS의 시스템 콜을 통해 파일을 읽고 쓰는 명령어를 OS 에게 전달한다.
- 시스템 콜은 상대적으로 무거운 작업이다.
- 디스크에 데이터를 한 번 읽고 쓸 때마다 필요한 시간이 있다.
=> 이러한 작업을 10 * 1024 * 1024 번 수행한다.

결론 : 1byte씩 읽고 쓴다면 많은 오버헤드와 실행 시간이 든다.
해결 : "버퍼" 라는 공간에 데이터를 담아 한 번에 여러 byte씩 데이터를 전달한다.
 */
