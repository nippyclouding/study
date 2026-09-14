package com.example.board.board.domain;

import jakarta.validation.constraints.NotBlank;
import lombok.*;
import org.hibernate.validator.constraints.Length;

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BoardRequestDto {
    @NotBlank
    private String title;
    @NotBlank
    private String writerName;
    @NotBlank
    private String content;
    @NotBlank @Length(min = 4, max = 4)
    private String password;
}
