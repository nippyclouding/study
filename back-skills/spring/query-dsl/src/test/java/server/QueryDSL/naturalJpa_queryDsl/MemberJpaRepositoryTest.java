package server.QueryDSL.naturalJpa_queryDsl;

import jakarta.persistence.EntityManager;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;
import server.QueryDSL.entity.Member;
import server.QueryDSL.entity.Team;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional
class MemberJpaRepositoryTest {
    @Autowired
    EntityManager em;

    @Autowired
    MemberJpaRepository memberJpaRepository;

    @Test
    void createAndSelectTest_naturalJpa() {
        //given
        Member member = new Member(10, "member1");
        memberJpaRepository.save(member); // auto increment : 바로 insert 쿼리가 전달된다.

        //when & then
        Member findMember = memberJpaRepository.findById(member.getId()).get();
        Assertions.assertThat(findMember).isEqualTo(member);

        //when & then
        List<Member> result1 = memberJpaRepository.findAll();
        Assertions.assertThat(result1).containsExactly(member);

        //when & then
        List<Member> result2 = memberJpaRepository.findByUserName(member.getUsername());
        Assertions.assertThat(result2).containsExactly(member);
    }

    @Test
    void createAndSelectTest_queryDsl() {
        // given
        Member member = new Member(10, "member2");

        memberJpaRepository.save(member);

        // when & then
        List<Member> result1 = memberJpaRepository.findAll_queryDsl();
        Assertions.assertThat(result1).containsExactly(member);

        // when & then
        List<Member> result2 = memberJpaRepository.findByUsername_queryDsl(member.getUsername());
        Assertions.assertThat(result2).containsExactly(member);
    }

    @Test
    void searchTest() {
        // given
        Team teamA = new Team("teamA");
        Team teamB = new Team("teamB");

        em.persist(teamA);
        em.persist(teamB);

        Member member1 = new Member(10, "member1", teamA);
        Member member2 = new Member(20, "member2", teamA);
        Member member3 = new Member(30, "member3", teamB);
        Member member4 = new Member(40, "member4", teamB);

        em.persist(member1);
        em.persist(member2);
        em.persist(member3);
        em.persist(member4);

        MemberSearchCondition cond = new MemberSearchCondition();
        cond.setAgeGoe(35);
        cond.setAgeLoe(40);
        cond.setTeamName("teamB");

        // when
        List<MemberTeamDto> result = memberJpaRepository.searchByBuilder(cond);

        // then
        Assertions.assertThat(result).extracting("username").containsExactly("member4");
    }
}