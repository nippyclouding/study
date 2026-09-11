package com.example.board.board.domain;

import com.example.board.comment.domain.Comment;
import lombok.*;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Board {
    private Long boardId;

    private String title;

    private String writerName;

    private String content;

    private String password;

    private LocalDateTime createdAt;

    private LocalDateTime deletedAt;
    @Builder.Default
    private List<Comment> comments = new ArrayList<>();
}
