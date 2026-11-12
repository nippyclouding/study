package shinhanproject.sh.ex3.domain;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@Getter
@ToString(exclude = "board")
@AllArgsConstructor
@NoArgsConstructor
public class Reply extends BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long rno;
    private String text;
    private String replyer;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "bno")
    private Board board;


}
