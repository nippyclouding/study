package buffered;

import java.io.*;

import static buffered.BufferedConst.*;

/*
기본 스트림 : 단독으로 사용 가능한 스트림, FileOutputStream ..
보조 스트림 : 단독으로 사용할 수 없고 보조 기능을 제공하는 스트림, BufferedOutputStream ..
보조 스트림은 생성자 파라미터로 기본 스트림을 전달하면서 생성한다.
new BufferedOutputStream(new FileOutputStream fos);
 */

public class CreateAndReadFileV3 {
    public static void main(String[] args) {
        FileOutputStream fileOutputStream = null;
        FileInputStream fileInputStream = null;

        BufferedOutputStream bufferedOutputStream = null;
        BufferedInputStream bufferedInputStream = null;

        try {
            fileOutputStream = new FileOutputStream(FILE_NAME);
            fileInputStream = new FileInputStream(FILE_NAME);

            // 8KB (8192 byte) 적재 가능한 버퍼
            // 파라미터 : 스트림 객체, 버퍼 사이즈
            bufferedOutputStream = new BufferedOutputStream(fileOutputStream, BUFFER_SIZE);
            bufferedInputStream = new BufferedInputStream(fileInputStream, BUFFER_SIZE);

            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < FILE_SIZE; i++) { // 10 * 1024 * 1024 번 반복
                bufferedOutputStream.write(1); // 8192 번 적재 후 버퍼 전송
            }
            // 버퍼가 가득 차면 write 메서드를 바로 자동 호출하며 쓰기 작업 후 버퍼를 비운다.
            // bufferedOutputStream.flush() : 버퍼가 다 차지 않아도 버퍼에 남은 데이터를 전달하는 메서드
            // bufferedOutputStream.close() : 먼저 flush 이후 버퍼를 비우고 닫고 자원 정리

            long endTime1 = System.currentTimeMillis();
            System.out.println("bufferedOutputStream 측정 시간 : " + (endTime1 - startTime1) + " ms");
            // 버퍼스트림 사용 -> 쓰기 시간 약 206ms 소요


            long startTime2 = System.currentTimeMillis();
            int size;
            boolean flag = true;
            while (flag) {
                size = bufferedInputStream.read(); // 버퍼에서 1byte씩 읽어오다 버퍼 크기만큼 차면 데이터를 읽어온다.
                if (size == -1) {
                    flag = false; // EoF일 때 flag를 false로 바꾸어 종료
                }
            }
            long endTime2 = System.currentTimeMillis();
            System.out.println("bufferedInputStream 측정 시간 : " + (endTime2 - startTime2) + " ms");

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                // bufferedStream 을 먼저 닫고 fileStream 을 닫아야 한다.
                // 그렇지 않으면 bufferedStream 의 flush 도 호출되지 않고 자원도 정리되지 않는다.
                if (bufferedOutputStream != null) bufferedOutputStream.close();
                if (bufferedInputStream != null) bufferedInputStream.close();
                if (fileOutputStream != null) fileOutputStream.close();
                if (fileInputStream != null) fileInputStream.close();
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
/*
BufferedOutputStream & BufferedInputStream은 단순히 버퍼 기능만 제공하며,
주 기능인 '스트림'을 생성자 파라미터로 전달해줘야 한다. (byte[] 배열을 파라미터로 직접 전달하지 X)

BufferedOutputStream & BufferedInputStream
extends FilterOutputStream & FilterInputStream
extends OutputStream & InputStream

FileOutputStream & FileInputStream
extends OutputStream & InputStream
 */

/*
-- 동기화
V2처럼 직접 버퍼 byte 배열을 생성했을 때보다는 성능이 좋지 않다.
원인은 write, read 메서드의 "동기화" 기능이기 때문이다.

동기화(Synchronization)는 여러 스레드가 동시에 같은 데이터에 접근할 때 데이터가 꼬이지 않도록 보호하는 기능이다.
동기화를 사용하면 한 번에 하나의 스레드만 공유 자원에 접근할 수 있다.
BufferedInputStream과 BufferedOutputStream은 안전한 버퍼 관리를 위해 내부적으로 동기화 등의 기능을 제공한다.
직접 구현한 byte[] 버퍼는 이러한 부가 기능이 없어 처리 과정의 오버헤드가 적다.
=> 성능만 비교하면 직접 구현한 버퍼가 BufferedInputStream, BufferedOutputStream 보다 약간 더 빠를 수 있다.

동기화를 사용하지 않으면 여러 스레드가 동시에 같은 데이터에 접근하여 값이 꼬이거나 데이터가 손상될 수 있다.
이러한 문제를 경쟁 상태(Race Condition)라고 한다.
동기화는 한 번에 하나의 스레드만 공유 자원에 접근하도록 제한한다.
=> 데이터의 일관성과 안정성을 보장할 수 있다.

동기화를 사용하지 않으면 여러 스레드가 동시에 같은 버퍼에 데이터를 읽거나 써서 버퍼 내용이 손상될 수 있다.
버퍼 내용이 손상되면 일부 데이터가 유실되거나 잘못 저장될 수 있다.
동기화는 한 번에 하나의 스레드만 버퍼에 접근하도록 제한한다.
=> 동기화를 통해 성능 부분에서는 손실이 나지만 버퍼의 데이터가 안전하게 관리되고 일관성이 유지된다.
 */