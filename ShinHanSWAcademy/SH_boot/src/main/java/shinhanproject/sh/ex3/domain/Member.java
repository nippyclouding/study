package shinhanproject.sh.ex3.domain;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Builder
@Getter
@ToString
@Table(name = "Members")
@AllArgsConstructor
@NoArgsConstructor
public class Member extends BaseEntity {
    @Id
    private String email;
    private String name;
    private String password;
}
