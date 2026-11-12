package spring.security.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import spring.security.entity.ClubMember;

public interface ClubMemberRepository extends JpaRepository<ClubMember, String> {
}
