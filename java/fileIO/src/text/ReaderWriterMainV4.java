package text;

import java.io.*;
import java.nio.charset.StandardCharsets;

import static text.TextConst.FILE_NAME;

public class ReaderWriterMainV4 {
    public static void main(String[] args) throws IOException {
        String s = "ABC\n가나디";
        System.out.println("원본 문자열 = " + s);

        FileWriter fw = new FileWriter(FILE_NAME, StandardCharsets.UTF_8);
        FileReader fr = new FileReader(FILE_NAME, StandardCharsets.UTF_8);

        BufferedWriter bw = new BufferedWriter(fw, 8192);
        BufferedReader br = new BufferedReader(fr, 8192);

        bw.write(s); // 쓰기
        bw.flush();

        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line).append("\n");
        }
        br.close();

        System.out.println(sb);


    }
}
