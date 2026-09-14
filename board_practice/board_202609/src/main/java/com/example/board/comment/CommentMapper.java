package com.example.board.comment;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface CommentMapper {
    void deleteCommentByBoardId(@Param("boardId") Long boardId);
}
