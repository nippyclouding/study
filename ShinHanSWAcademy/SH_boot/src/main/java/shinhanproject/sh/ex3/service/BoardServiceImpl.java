package shinhanproject.sh.ex3.service;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;
import shinhanproject.sh.ex3.domain.Board;
import shinhanproject.sh.ex3.domain.Member;
import shinhanproject.sh.ex3.dto.BoardDto;
import shinhanproject.sh.ex3.dto.PageRequestDto;
import shinhanproject.sh.ex3.dto.PageResultDto;
import shinhanproject.sh.ex3.repository.BoardRepository;
import shinhanproject.sh.ex3.repository.MemberRepository;
import shinhanproject.sh.ex3.repository.ReplyRepository;

import java.util.function.Function;

@Service
@RequiredArgsConstructor
public class BoardServiceImpl implements BoardService {

    private final BoardRepository boardRepository;
    private final MemberRepository memberRepository;
    private final ReplyRepository replyRepository;

    @Override
    public Long register(BoardDto dto) {
        Member member = memberRepository.getReferenceById(dto.getWriterEmail()); // findById는 즉시 select 쿼리 실행, getReferenceById는 프록시 반환 후 데이터 접근 시 select 실행
        return boardRepository.save(dtoToEntity(dto, member)).getBno();
    }

    @Override
    public PageResultDto<BoardDto, Object[]> getList(PageRequestDto dto) {
        Function<Object[], BoardDto> function = (en -> entityToDto((Board) en[0], (Member) en[1], (Long) en[2]));
        Page<Object[]> result = boardRepository.getBoardWithReplyCount(dto.getPageable(Sort.by("bno").descending()));

        return new PageResultDto<>(result, function);
    }

    @Transactional
    @Override
    public void removeWithReplies(Long bno) {
        replyRepository.deleteById(bno);
        boardRepository.deleteById(bno);
    }

    @Override
    public void modify(BoardDto dto) {
        Board board = boardRepository.getReferenceById(dto.getBno());
        if (board != null) {
            board.changeTitle(dto.getTitle());
            board.changeContent(dto.getContent());

            boardRepository.save(board);
        }
    }

    @Override
    public BoardDto get(Long bno) {
        Object result = boardRepository.getBoardByBno(bno);
        Object[] arr = (Object[]) result;

        return entityToDto((Board) arr[0], (Member) arr[1], (Long) arr[2]);
    }
}
