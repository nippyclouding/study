package shinhanproject.sh.ex2.service;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import shinhanproject.sh.ex2.domain.GuestBook;
import shinhanproject.sh.ex2.dto.GuestBookDto;
import shinhanproject.sh.ex2.dto.PageRequestDto;
import shinhanproject.sh.ex2.dto.PageResultDto;
import shinhanproject.sh.ex2.repository.GuestBookRepository;

import java.util.Optional;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class GuestBookServiceImplTest {

    @Autowired
    GuestBookService guestBookService;
    @Autowired
    GuestBookRepository guestBookRepository;

    @Test
    void register() {
        //given
        GuestBookDto testDto = GuestBookDto.builder()
                .title("hello")
                .content("hello")
                .writer("kim")
                .build();
        //when
        Long registeredId = guestBookService.register(testDto);

        Optional<GuestBook> byId = guestBookRepository.findById(registeredId);
        GuestBook guestBook = byId.get();

        //then
        assertThat(guestBook.getId().equals(registeredId));
    }

    @Test
    void getList() {
        PageRequestDto pageRequestDto = PageRequestDto.builder()
                .page(1)
                .size(10)
                .build();
        PageResultDto<GuestBookDto, GuestBook> resultDto = guestBookService.getList(pageRequestDto);

        for (GuestBookDto dto : resultDto.getDtos()) {
            System.out.println(dto);
        }
    }
}