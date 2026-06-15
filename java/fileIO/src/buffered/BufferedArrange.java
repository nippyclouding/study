package buffered;

import java.io.*;
import java.util.Arrays;

public class BufferedArrange {
    public static void main(String[] args) {

        try {
            FileOutputStream fos = new FileOutputStream("temp/test_arrange.dat");
            FileInputStream fis = new FileInputStream("temp/test_arrange.dat");

            BufferedOutputStream bos = new BufferedOutputStream(fos);
            BufferedInputStream bis = new BufferedInputStream(fis);


            // 1. byte[] 배열 읽고 쓰기
            byte[] bytes = new byte[5 * 1024 * 1024];
            long startTime1 = System.currentTimeMillis();
            for (int i = 0; i < bytes.length; i++) {
                fos.write(1);
            }
            long endTime1 = System.currentTimeMillis();
            System.out.println((endTime1 - startTime1) + " ms");

            int temp;
            long startTime2 = System.currentTimeMillis();
            while ((temp = fis.read()) != -1) {

            }

            long endTime2 = System.currentTimeMillis();
            System.out.println((endTime2 - startTime2) + " ms");

            // 2. buffered 를 이용한 읽고 쓰기

            long startTime3 = System.currentTimeMillis();
            for (int i = 0; i < bytes.length; i++) {
                bos.write(1);
            }
            bos.flush();
            long endTime3 = System.currentTimeMillis();
            System.out.println((endTime3 - startTime3) + " ms");

            long startTime4 = System.currentTimeMillis();
            while ((temp = bis.read()) != -1) {

            }
            long endTime4 = System.currentTimeMillis();
            System.out.println((endTime4 - startTime4) + " ms");

            // 3. byte[] 배열을 버퍼로 쓰기
            byte[] bufferArray = new byte[1 * 1024 * 1024];
            fos = new FileOutputStream("temp/test_arrange.dat");
            fis = new FileInputStream("temp/test_arrange.dat");


            int bufferIndex = 0;

            long startTime5 = System.currentTimeMillis();
            for (int i = 0; i < 5 * 1024 * 1024; i++) {

                bufferArray[bufferIndex++] = 1;

                if (bufferIndex == bufferArray.length) {
                    fos.write(bufferArray);
                    bufferIndex = 0;
                }
            }

            if (bufferIndex > 0) {
                fos.write(bufferArray, 0, bufferIndex);
            }
            long endTime5 = System.currentTimeMillis();
            System.out.println((endTime5 - startTime5) + " ms");


            long startTime6 = System.currentTimeMillis();
            int totalRead = 0;                       // 전체 읽은 바이트 수
            int readBytes;                           // 이번에 실제 읽은 바이트 수

            while ((readBytes = fis.read(bufferArray)) != -1) {

                totalRead += readBytes;

                // 버퍼 안의 실제 읽은 데이터 처리
                for (int i = 0; i < readBytes; i++) {
                }
            }
            long endTime6 = System.currentTimeMillis();

            System.out.println((endTime6 - startTime6) + " ms");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static void clean(byte[] bufferArray) {
        for (int i = 0; i < bufferArray.length; i++) {
            bufferArray[i] = 0;
        }
    }

    private static boolean isFilled(byte[] bufferArray) {
        return bufferArray[bufferArray.length - 1] != 0;
    }
}
