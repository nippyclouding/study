package shinhanproject.sh.ex3.service;

import shinhanproject.sh.ex3.domain.Board;
import shinhanproject.sh.ex3.domain.Member;
import shinhanproject.sh.ex3.dto.BoardDto;
import shinhanproject.sh.ex3.dto.PageRequestDto;
import shinhanproject.sh.ex3.dto.PageResultDto;

public interface BoardService {
    Long register(BoardDto dto); // dto로 값을 받아 board 엔티티 저장

    PageResultDto<BoardDto, Object[]> getList(PageRequestDto dto);

    void removeWithReplies(Long bno);

    void modify(BoardDto dto);

    default Board dtoToEntity(BoardDto dto, Member member) {
        return Board.builder()
                .bno(dto.getBno())
                .title(dto.getTitle())
                .content(dto.getContent())
                .writer(member)
                .build();
    }

    default BoardDto entityToDto(Board board, Member member, Long replyCount) {
        return BoardDto.builder()
                .bno((board.getBno()))
                .title(board.getTitle())
                .content(board.getContent())
                .registerDate(board.getRegisterDate())
                .modulateDate(board.getModDate())
                .writerEmail(member.getEmail())
                .writerName(member.getName())
                .replyCount(replyCount.intValue())
                .build();
    }

    BoardDto get(Long bno);
}
