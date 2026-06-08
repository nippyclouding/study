package shinhanproject.sh.ex2.service;

import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import shinhanproject.sh.ex2.domain.GuestBook;
import shinhanproject.sh.ex2.dto.GuestBookDto;
import shinhanproject.sh.ex2.dto.PageRequestDto;
import shinhanproject.sh.ex2.dto.PageResultDto;
import shinhanproject.sh.ex2.repository.GuestBookRepository;

import java.util.function.Function;

@RequiredArgsConstructor
@Service
public class GuestBookServiceImpl implements GuestBookService{

    private final GuestBookRepository guestBookRepository;

    @Override
    public Long register(GuestBookDto dto) {
        return guestBookRepository.save(dtoToEntity(dto)).getId();
    }

    @Override
    public PageResultDto<GuestBookDto, GuestBook> getList(PageRequestDto dto) {
        Pageable pageable = dto.getPageable(Sort.by("id").descending());

        Page<GuestBook> result = guestBookRepository.findAll(pageable);

        Function<GuestBook, GuestBookDto> function = (entity -> entityToDto(entity));

        return new PageResultDto<>(result, function);
    }
}
