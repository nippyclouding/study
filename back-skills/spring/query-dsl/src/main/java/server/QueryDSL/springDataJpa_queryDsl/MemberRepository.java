package server.QueryDSL.springDataJpa_queryDsl;

import org.springframework.data.jpa.repository.JpaRepository;
import server.QueryDSL.entity.Member;

import java.util.List;

public interface MemberRepository extends JpaRepository<Member, Long>, MemberRepositoryCustom {
    List<Member> findByUsername(String username);
}
