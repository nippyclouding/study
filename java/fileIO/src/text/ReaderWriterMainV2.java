package text;

import java.io.*;
import java.nio.charset.StandardCharsets;

import static text.TextConst.FILE_NAME;

public class ReaderWriterMainV2 {
    public static void main(String[] args) throws IOException {
        String s = "ABC";
        FileOutputStream fos = new FileOutputStream(FILE_NAME);
        FileInputStream fis = new FileInputStream(FILE_NAME);

        OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8); // 보조 스트림
        InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8); // 보조 스트림

        osw.write(s);
        // osw.flush();
        osw.close();

        StringBuilder sb = new StringBuilder();
        int idx;
        while ((idx = isr.read()) != -1) {
            sb.append((char) idx); // isr.read()는 int 형으로 데이터를 읽는다 (A : 65 ..) =>
        }

        // osw.close();
        isr.close();
        System.out.println(sb);
    }
}

/* osw.flush를 하거나 close로 닫아주어야 inputStreamReader가 읽을 수 있다.
inputStreamReader가 먼저 읽은 뒤 osw.close 를 한다면 flush가 되지 않은 상태에서 읽기를 시도하기에 데이터를 읽어들일 수 없다.

OutputStreamReader, InputStreamReader 은 보조 스트림 역할을 한다.
메인 스트림으로 데이터를 주고 받을 떄 byte <-> UTF8 등 문자 형태를 개발자가 매번 지정해주지 않고,
보조 스트림으로 한 번 지정해주면 매 번 사용할 수 있다.

메인 스트림은 바이트 단위로만 데이터를 보낸다.
InputStreamReader, OutputStreamWriter 보조 스트림을 이용하면 선언할 때 한 번만 인코딩 방식을 지정해두면
변환 과정을 신경쓰지 않고 계속 쓸 수 있다.

클라이언트 데이터(String) -> OutputStreamWriter(UTF8) (문자를 바이트로 인코딩) -> FileOutputStream (바이트를 파일에 기록)
FileInputStream (파일에서 바이트를 읽어옴) -> InputStreamReader(UTF8) (바이트를 문자로 디코딩) -> 프로그램/개발자(char/String)
 */

