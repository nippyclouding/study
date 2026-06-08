package fileIOEx;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class StreamStartMain1 {
    public static void main(String[] args) throws IOException {
        // test1.dat에 데이터를 쓸 객체
        FileOutputStream fos = new FileOutputStream("temp/test1.dat");

        // 아스키 코드는 byte 숫자 형태이다.
        fos.write(65); // A
        fos.write(66); // B
        fos.write(67); // C

        // test1.dat 데이터를 읽을 객체
        FileInputStream fis = new FileInputStream("temp/test1.dat");

        System.out.println(fis.read()); // 바이트 코드 출력 : 65
        System.out.println(fis.read()); // 바이트 코드 출력 : 66
        System.out.println(fis.read()); // 바이트 코드 출력 : 67
        System.out.println(fis.read()); // -1 출력 : 더이상 출력할 데이터가 없다면 -1 출력 (End OF File EOF)

        // true 옵션 : 기존 파일에 이어쓰기
        FileOutputStream fos2 = new FileOutputStream("temp/test1.dat", true);
        fos2.write(68);
        System.out.println(fis.read()); // 68 출력

        /* OS 자원 반납, 외부 자원 (OS 자원)을 이용할 때는 반드시 닫아야 한다.
        자바의 GC: JVM 내부에 있는 힙 메모리만 관리 (JVM : Class, Stack, Heap)
        스트림 객체 : 생성되는 순간 OS 로부터 파일 핸들이나 파일 디스크립터 같은 외부 시스템 자원을 빌려온다.
        GC는 자바 객체 자체는 소멸시킬 수 있지만 OS가 빌려준 파일 핸들까지 자동으로 반납해 주지는 못한다.

        OS 자원을 반납하지 않을 경우 OS 파일 시스템 자원이 가득 차서 새로운 파일을 열 수 없게 될 수도 있다.
        ex : 식별 번호(File Descriptor) 를 사용 가능한 객체는 한정적인데, close로 자원을 반납하지 않으면 새로운 파일 입출력 객체를 생성하지 못할 수도 있다.
        정확히는 객체는 생성 가능하지만 파일을 읽어오려는 순간 IOException (Too many open files) 발생
        FileOutputStream 경우 버퍼에 남아있던 데이터가 출력되지 않거나 다른 프로세스가 해당 파일을 수정, 삭제하지 못하도록 락을 걸 수 있어 문제
         */
        fos.close();
        fis.close();

        // 회사에서 자주 쓰는 코드
        FileInputStream repeat = new FileInputStream("temp/test1.dat");
        int data;
        while ((data = repeat.read()) != -1) {
            System.out.println(data);
        }
    }
}
