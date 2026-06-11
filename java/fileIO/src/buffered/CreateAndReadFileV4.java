package buffered;

import java.io.*;

import static buffered.BufferedConst.*;

public class CreateAndReadFileV4 {
    public static void main(String[] args) {
        FileOutputStream fileOutputStream = null;
        FileInputStream fileInputStream = null;

        try {
            fileOutputStream = new FileOutputStream(FILE_NAME);
            fileInputStream = new FileInputStream(FILE_NAME);

            long startTime1 = System.currentTimeMillis();
            // 파일 크기가 크지 않다면 버퍼에 쓴 뒤 한 번에 전달
            byte[] buffer = new byte[FILE_SIZE]; // 10 * 1024 * 1024
            for (int i = 0; i < FILE_SIZE; i++) {
                buffer[i] = 1;
            }
            // 가득 찬 buffer로 한 번에 파일 쓰기
            fileOutputStream.write(buffer);
            long endTime1 = System.currentTimeMillis();
            System.out.println("버퍼에 데이터를 모두 담아 한 번에 전달할 때의 시간 : " + (endTime1 - startTime1) + " ms"); // 36ms
            // 파일 크기가 크지 않다면 버퍼에 가득 쓴 뒤 한 번에 전달하는 방법도 효율적이다.
            // OS 레벨에서 파일 쓰고 읽기는 보통 한 번에 8kb 만큼만 쓰고 읽기에 버퍼에 많이 담아서 한 번에 써도 더 빨라지는 것은 아니다.

            long startTime2 = System.currentTimeMillis();
            byte[] bytes = fileInputStream.readAllBytes(); // readAllBytes로 한 번에 읽어올 수 있다 (최대 8kb)
            long endTime2 = System.currentTimeMillis();
            System.out.println("readAllBytes로 한 번에 읽어올 경우 : " + (endTime2 - startTime2) + " ms");

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (fileOutputStream != null) fileOutputStream.close();
                if (fileInputStream != null) fileInputStream.close();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}

/*
파일 크기가 크지 않아 메모리 사용에 큰 영향을 주지 않을 경우에는 해당 방식처럼 빠르게 한 번에 처리 가능
성능이 중요한 부분에서는 buffer stream을 쓰기보다 지금처럼 byte[] 배열의 버퍼를 직접 다루는 것이 효율적이다.
성능이 크게 중요하지 않은 부분에서 버퍼 기능이 필요할 때 buffer stream 사용 권장
buffer stream은 동기화 코드가 들어가있기에 스레드에 안전하지만 byte[] 배열을 직접 다루는 것보다는 성능이 조금 떨어진다.
 */