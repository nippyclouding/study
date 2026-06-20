package text;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

import static text.TextConst.FILE_NAME;

public class ReaderWriterMainV3 {
    public static void main(String[] args) throws IOException {
        String s = "ABC";
        System.out.println("원본 문자열 = " + s);

        FileWriter fw = new FileWriter(FILE_NAME, StandardCharsets.UTF_8);
        FileReader fr = new FileReader(FILE_NAME, StandardCharsets.UTF_8);

        fw.write(s);
        fw.flush(); // fw.close

        StringBuilder sb = new StringBuilder();
        int ch;
        while ((ch = fr.read()) != -1) {
            sb.append((char) ch);
        }
        System.out.println("FileReader 로 읽은 문자열 = " + sb);
        fw.close();
        fr.close();
    }
}
