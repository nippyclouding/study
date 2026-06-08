package server.QueryDSL.naturalJpa_queryDsl;

import com.querydsl.core.BooleanBuilder;
import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import jakarta.persistence.EntityManager;
import org.springframework.stereotype.Repository;
import server.QueryDSL.entity.Member;
import server.QueryDSL.entity.QMember;
import server.QueryDSL.entity.QTeam;
import server.QueryDSL.springDataJpa_queryDsl.MemberSearchCond;

import java.util.List;
import java.util.Optional;

import static io.micrometer.common.util.StringUtils.isEmpty;
import static org.springframework.util.StringUtils.hasText;

@Repository
public class MemberJpaRepository {
    private final EntityManager em;
    private final JPAQueryFactory queryFactory;

    public MemberJpaRepository(EntityManager em) {
        this.em = em;
        this.queryFactory = new JPAQueryFactory(em);
    }

    // 기본 JPA 메서드
    public void save(Member member) {
        em.persist(member);
    }

    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(em.find(Member.class, id));
    }

    public List<Member> findByUserName(String username) {
        return em.createQuery("select m from Member m where m.username = :username", Member.class)
                .setParameter("username", username)
                .getResultList();
    }

    public List<Member> findAll() {
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }

    // QueryDsl
    public List<Member> findAll_queryDsl() {
        QMember qMember = QMember.member;
        return queryFactory.selectFrom(qMember).fetch();
    }

    public List<Member> findByUsername_queryDsl(String username) {
        QMember qMember = QMember.member;
        return queryFactory.selectFrom(qMember)
                .where(qMember.username.eq(username))
                .fetch();
    }


    public List<MemberTeamDto> searchByBuilder(MemberSearchCondition cond) {
        QMember qMember = QMember.member;
        QTeam qTeam = QTeam.team;
        BooleanBuilder builder = new BooleanBuilder();

        if (hasText(cond.getUsername())) builder.and(qMember.username.eq(cond.getUsername()));
        if (hasText(cond.getTeamName())) builder.and(qTeam.name.eq(cond.getTeamName()));
        if (cond.getAgeGoe() != null) builder.and(qMember.age.goe(cond.getAgeGoe()));
        if (cond.getAgeLoe() != null) builder.and(qMember.age.goe(cond.getAgeLoe()));

        return queryFactory
                .select(new QMemberTeamDto(
                        qMember.id,
                        qMember.username,
                        qMember.age,
                        qTeam.id,
                        qTeam.name))
                .from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(builder)
                .fetch();
    }

    public List<MemberTeamDto> search(MemberSearchCondition cond) {
        QMember qMember = QMember.member;
        QTeam qTeam = QTeam.team;

        BooleanExpression usernameEq = isEmpty(cond.getUsername()) ? null : qMember.username.eq(cond.getUsername());
        BooleanExpression teamNameEq = isEmpty(cond.getTeamName()) ? null : qTeam.name.eq(cond.getTeamName());
        BooleanExpression ageGoe = cond.getAgeGoe() == null ? null : qMember.age.goe(cond.getAgeGoe());
        BooleanExpression ageLoe = cond.getAgeLoe() == null ? null : qMember.age.loe(cond.getAgeLoe());

        return queryFactory.select(new QMemberTeamDto(
                qMember.id,
                qMember.username,
                qMember.age,
                qTeam.id,
                qTeam.name))
                .from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(usernameEq, teamNameEq, ageGoe, ageLoe)
                .fetch();
    }
}
