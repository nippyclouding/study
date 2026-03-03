package shinhanproject.sh.ex2.service;

import shinhanproject.sh.ex2.domain.GuestBook;
import shinhanproject.sh.ex2.dto.GuestBookDto;
import shinhanproject.sh.ex2.dto.PageRequestDto;
import shinhanproject.sh.ex2.dto.PageResultDto;

public interface GuestBookService {
    Long register(GuestBookDto dto);
    PageResultDto<GuestBookDto, GuestBook> getList(PageRequestDto dto);

    default GuestBook dtoToEntity(GuestBookDto dto) {
        return GuestBook.builder()
                .title(dto.getTitle())
                .content(dto.getContent())
                .writer(dto.getWriter())
                .build();
    }

    default GuestBookDto entityToDto(GuestBook book) {
        return GuestBookDto.builder()
                .id(book.getId())
                .writer(book.getWriter())
                .content(book.getContent())
                .title(book.getTitle())
                .registerDate(book.getRegisterDate())
                .modulateDate(book.getModDate())
                .build();
    }
}
