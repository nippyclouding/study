package shinhanproject.sh.ex3.service;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import shinhanproject.sh.ex3.domain.Member;
import shinhanproject.sh.ex3.dto.BoardDto;
import shinhanproject.sh.ex3.dto.PageRequestDto;
import shinhanproject.sh.ex3.dto.PageResultDto;
import shinhanproject.sh.ex3.repository.MemberRepository;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class BoardServiceImplTest {

    @Autowired
    private BoardService boardService;

    @Autowired
    private MemberRepository memberRepository;

    @Test
    void register() {
        memberRepository.save(Member.builder()
                .email("user55@aaa.com")
                .name("User55")
                .password("1111")
                .build());

        BoardDto dto = BoardDto.builder()
                .title("Test.")
                .content("Test...")
                .writerEmail("user55@aaa.com")
                .build();

        Long bno = boardService.register(dto);
    }

    @Test
    public void testList() {
        PageRequestDto pageRequestDto = new PageRequestDto();
        PageResultDto<BoardDto, Object[]> list = boardService.getList(pageRequestDto);

        for (BoardDto dto : list.getDtos()) System.out.println(dto);

    }
}