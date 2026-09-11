package com.example.board.comment.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Comment {
    private Long commentId;

    private Long boardId;

    private String content;

    private String password;

    private String writerName;

    private LocalDateTime createdAt;

    private LocalDateTime deletedAt;
}
