package shinhanproject.sh.ex3.dto;

import lombok.*;

import java.time.LocalDateTime;

@Data
@Builder
@ToString
@AllArgsConstructor
@NoArgsConstructor
public class BoardDto {
    private Long bno;
    private String title;
    private String content;
    private String writerEmail;
    private String writerName;
    private LocalDateTime registerDate;
    private LocalDateTime modulateDate;
    private int replyCount;
}
