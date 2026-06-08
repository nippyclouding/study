package shinhanproject.sh.ex3.repository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import shinhanproject.sh.ex3.domain.Board;
import shinhanproject.sh.ex3.domain.Member;

import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class BoardRepositoryTest {

    @Autowired
    BoardRepository boardRepository;
    @Autowired
    MemberRepository memberRepository;

    @Test
    void insertBoard() {
        //given
        IntStream.rangeClosed(1, 100).forEach(i -> {
            Member member = Member.builder().email("user" + i + "aaa.com").build();

            memberRepository.save(member);

            Board board = Board.builder()
                    .title("title " + i)
                    .content("content .. " + i)
                    .writer(member)
                    .build();

        //when & then
        boardRepository.save(board);
        });
    }

    @Test
    void testTreadWithWriter() {
        //given
        Object result = boardRepository.getBoardWithWriter(100L);

        //when
        Object[] arr = (Object[]) result;

        //then
        System.out.println(Arrays.toString(arr));

    }

    @Test
    void testGetBoardWithReply() {
        //given
        List<Object[]> result = boardRepository.getBoardWithReply(100L);

        //when



        //then
        for (Object[] arr : result) {
            System.out.println(Arrays.toString(arr));
        }

    }

}