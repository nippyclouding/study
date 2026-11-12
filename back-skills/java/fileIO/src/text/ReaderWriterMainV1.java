package text;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

import static text.TextConst.FILE_NAME;

public class ReaderWriterMainV1 {
    public static void main(String[] args) throws IOException {
        String s = "ABC";

        // s.getBytes(UTF8) : 문자 -> byte 인코딩
        byte[] writeBytes = s.getBytes(StandardCharsets.UTF_8);
        // byte 배열 속 byte 데이터를 toString 으로 출력 : [65, 66, 67], String 형태가 아닌 Byte 형태로 출력된다.
        System.out.println("write bytes: " + Arrays.toString(writeBytes));

        // byte 배열 속 byte 데이터를 toString 없이 그대로 출력 : [B@7291c18f
        System.out.println("writeBytes = " + writeBytes);

        FileOutputStream fos = new FileOutputStream(FILE_NAME);
        FileInputStream fis = new FileInputStream(FILE_NAME);

        fos.write(writeBytes); // 파일에 바이트 배열 쓰기
        fos.close();

        byte[] readBytes = fis.readAllBytes();// 파일속 데이터를 모두 읽어온다.
        fis.close();

        // byte 배열 -> String Utf8 디코딩, new String (byte[], 인코딩 문자 형태)
        String readString = new String(readBytes, StandardCharsets.UTF_8);
        System.out.println(readString); // 문자열 출력
    }
}

/*
스트림은 byte만 다룰 수 있기 때문에 String 등 문자 데이터는 전달할 수 없다.
이번 예시처럼 직접 변환할 수도 있지만 Buffered 보조 스트림을 통해 String <-> byte 를 쉽게 변환할 수 있다.
 */
