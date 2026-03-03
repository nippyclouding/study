package shinhanproject.sh.ex3.repository;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import shinhanproject.sh.ex3.domain.Board;
import shinhanproject.sh.ex3.domain.Member;
import shinhanproject.sh.ex3.domain.Reply;

import java.util.stream.IntStream;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class ReplyRepositoryTest {
    @Autowired
    ReplyRepository replyRepository;
    @Autowired
    BoardRepository boardRepository;
    @Autowired
    MemberRepository memberRepository;

    @Test
    void insertReply() {
        IntStream.rangeClosed(1, 100).forEach(i -> {
            Member member = Member.builder().email("user" + i + "aaa.com").build();
            memberRepository.save(member);
            Board board = Board.builder()
                    .title("title " + i)
                    .content("content " + i)
                    .writer(member)
                    .build();
            boardRepository.save(board);
            //when & then

            Reply reply = Reply.builder()
                    .text("reply .. " + i)
                    .board(board)
                    .replyer("guest")
                    .build();

            replyRepository.save(reply);
        });
    }
}