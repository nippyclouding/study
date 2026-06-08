package shinhanproject.sh.ex2.dto;

import lombok.Data;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Data
public class PageResultDto<DTO, EN> {
    private List<DTO> dtos;

    private int totalPage;

    private int page;
    private int size;

    private int start;
    private int end;

    private boolean prev;
    private boolean next;

    private List<Integer> pages;

    public PageResultDto(Page<EN> result, Function<EN, DTO> fn) {
        dtos = result.stream().map(fn).collect(Collectors.toList());
        totalPage = result.getTotalPages();
        makePageList(result.getPageable());
    }

    private void makePageList(Pageable pageable) {
        page = pageable.getPageNumber() + 1;
        size = pageable.getPageSize();

        int tempEnd = (int) (Math.ceil(page / 10.0)) * 10;

        start = tempEnd - 9;

        prev = start > 1;
        end = totalPage > tempEnd ? tempEnd : totalPage;

        next = totalPage > tempEnd;

        pages = IntStream.rangeClosed(start, end).boxed().collect(Collectors.toList());
    }
}
