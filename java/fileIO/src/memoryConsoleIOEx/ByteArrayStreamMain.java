package memoryConsoleIOEx;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class ByteArrayStreamMain {
    public static void main(String[] args) {
        byte[] input = {1, 2, 3};

        ByteArrayOutputStream byteArrayOutputStream = null;
        ByteArrayInputStream byteArrayInputStream = null;

        PrintStream printStream = null;
        try {

            System.out.println("=============메모리 스트림============");
            // 메모리 쓰기, 읽기 (컬렉션이나 배열을 사용하여 메모리에서 비교할 수 있기에 자주 사용하진 X)
            // 메모리에 쓰기
            byteArrayOutputStream = new ByteArrayOutputStream();
            byteArrayOutputStream.write(input); // 1, 2, 3을 메모리에 쓴다.

            // 메모리에 쓰여진 1, 2, 3을 읽어오는 객체
            byteArrayInputStream =
                    new ByteArrayInputStream(byteArrayOutputStream.toByteArray()); // 입력 스트림.toByteArray

            byte[] bytes = byteArrayInputStream.readAllBytes(); // 읽어온 1, 2, 3을 배열에 담는다.
            System.out.println(Arrays.toString(bytes));


            System.out.println("=============콘솔 스트림============");
            printStream = System.out; // System.out = PrintStream (콘솔 스트림), extends OutputStream을 하고 있다.
            byte[] data = "Hello! \n".getBytes(StandardCharsets.UTF_8);
            printStream.write(data); // Hello! 출력
            printStream.println("Print!"); // System.out.println("Print!")

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if (byteArrayOutputStream != null) {
                    byteArrayOutputStream.close();
                }
                if (byteArrayInputStream != null) {
                    byteArrayInputStream.close();
                }
                if (printStream != null) {
                    printStream.close();
                    /*
                    System.out, System.err를 받은 PrintStream 일 경우 함부로 닫으면 문제가 된다.
                    printStream 객체가 가지는 Stream 의 관리 주체가 JVM 이다.
                    JVM이 OS와 연결해 둔 콘솔 통로 자체가 끊어져 close 이후 System.out.println 시 출력되지 X

                    파일이나 네트워크 소켓을 열어서 만든 PrintStream일 경우 외부 자원을 사용하기에 반드시 직접 닫아야 한다.
                     */
                }
            } catch (IOException e) {
                System.out.println(e.getMessage());
            }
        }

    }
}
