package shinhanproject.sh.ex3.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import shinhanproject.sh.ex3.domain.Reply;

public interface ReplyRepository extends JpaRepository<Reply, Long> {
}
