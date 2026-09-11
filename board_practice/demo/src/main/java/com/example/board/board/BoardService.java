package com.example.board.board;

import com.example.board.board.domain.Board;
import com.example.board.board.domain.BoardRequestDto;
import com.example.board.comment.CommentMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;

import static com.example.board.util.EncryptPassword.encryptSHA256;

@Transactional(readOnly = true)
@RequiredArgsConstructor
@Service
@Slf4j
public class BoardService {

    private final static int PAGING_COUNT = 5;

    private final BoardMapper boardMapper;
    private final CommentMapper commentMapper;

    public List<Board> getMainBoardsByPaging(int currentPage) {
        int offset = currentPage * PAGING_COUNT;
        return boardMapper.findMainBoardsByPaging(PAGING_COUNT, offset);
    }

    public int getCount() {
        return boardMapper.findAllCount();
    }

    public Board getBoardDetail(Long boardId) {
        return boardMapper.findBoardByIdWithComments(boardId);
    }

    public boolean checkPassword(String password, Long boardId) {
        String encryptPassword = encryptSHA256(password);

        Board findBoard = boardMapper.findBoardById(boardId);

        if (findBoard == null || findBoard.getPassword().isEmpty()) {
            return false;
        }

        if (findBoard.getPassword().equals(encryptPassword)) {
            return true;
        } else return false;
    }

    @Transactional
    public boolean createBoard(BoardRequestDto dto) {
        Board board = dtoToBoard(dto);
        int successCount = boardMapper.insertBoard(board);

        return successCount == 1;
    }

    @Transactional
    public boolean updateBoard(Long boardId, BoardRequestDto dto, String password) {
        if (!checkPassword(password, boardId)) {
            return false;
        }

        Board board = dtoToBoard(dto);
        int successCount = boardMapper.updateBoard(board, boardId);
        return successCount == 1;
    }

    @Transactional
    public boolean deleteBoard(Long boardId) {
        Board findBoard = boardMapper.findBoardById(boardId);

        // 1. delete comment
        commentMapper.deleteCommentByBoardId(boardId);

        // 2. delete board
        int successCount = boardMapper.deleteBoardByBoardId(boardId);

        return successCount == 1;
    }


    private Board dtoToBoard(BoardRequestDto dto) {
        return Board.builder()
                .title(dto.getTitle())
                .content(dto.getContent())
                .writerName(dto.getWriterName())
                .password(encryptSHA256(dto.getPassword()))
                .build();
    }
}
