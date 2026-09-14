package com.example.board.board;

import com.example.board.board.domain.Board;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface BoardMapper {
    List<Board> findMainBoardsByPaging(@Param("pagingCount") int pagingCount,
                                       @Param("offset") int offset);

    int findAllCount();

    Board findBoardByIdWithComments(@Param("boardId") Long boardId);

    int insertBoard(@Param("board") Board board);

    int updateBoard(@Param("board") Board board, @Param(("boardId")) Long boardId);

    Board findBoardById(@Param("boardId") Long boardId);

    int deleteBoardByBoardId(@Param("boardId") Long boardId);
}
