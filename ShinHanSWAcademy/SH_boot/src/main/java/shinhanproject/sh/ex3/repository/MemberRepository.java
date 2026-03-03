package shinhanproject.sh.ex3.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import shinhanproject.sh.ex3.domain.Member;

public interface MemberRepository extends JpaRepository<Member, String> {
}
