package shinhanproject.sh.ex3.domain;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@Getter
@ToString(exclude = "writer")
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "Boards")
public class Board extends BaseEntity {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long bno;
    private String title;
    private String content;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "writer_email")
    private Member writer;
}
