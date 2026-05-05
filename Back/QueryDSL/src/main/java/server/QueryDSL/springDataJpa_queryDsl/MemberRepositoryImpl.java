package server.QueryDSL.springDataJpa_queryDsl;

import com.querydsl.core.QueryResults;
import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.jpa.impl.JPAQuery;
import com.querydsl.jpa.impl.JPAQueryFactory;
import jakarta.persistence.EntityManager;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;
import org.springframework.data.support.PageableExecutionUtils;
import server.QueryDSL.entity.Member;
import server.QueryDSL.entity.QMember;
import server.QueryDSL.entity.QTeam;
import server.QueryDSL.naturalJpa_queryDsl.MemberSearchCondition;

import java.util.List;

import static io.micrometer.common.util.StringUtils.isEmpty;

public class MemberRepositoryImpl implements MemberRepositoryCustom {

    private final JPAQueryFactory queryFactory;

    public MemberRepositoryImpl(EntityManager em) {
        this.queryFactory = new JPAQueryFactory(em);
    }

    @Override
    public List<MemberTeamDto> search(MemberSearchCond cond) {
        QMember qMember = QMember.member;
        QTeam qTeam = QTeam.team;

        BooleanExpression userNameEq = isEmpty(cond.getUsername()) ? null : qMember.username.eq(cond.getUsername());
        BooleanExpression teamNameEq = isEmpty(cond.getTeamName()) ? null : qTeam.name.eq(cond.getTeamName());
        BooleanExpression ageGoe = cond.getAgeGoe() == null ? null : qMember.age.goe(cond.getAgeGoe());
        BooleanExpression ageLoe = cond.getAgeLoe() == null ? null : qMember.age.loe(cond.getAgeLoe());


        List<MemberTeamDto> result =
                queryFactory.select(new QMemberTeamDto(
                        qMember.id, qMember.username, qMember.age, qTeam.id, qTeam.name))
                .from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(userNameEq, teamNameEq, ageGoe, ageLoe) // 동적 쿼리
                .fetch();

        return result;
    }

    @Override
    public Page<MemberTeamDto> searchPageSimple(MemberSearchCondition cond, Pageable pageable) {
        QMember qMember = QMember.member;
        QTeam qTeam = QTeam.team;

        BooleanExpression userNameEq = isEmpty(cond.getUsername()) ? null : qMember.username.eq(cond.getUsername());
        BooleanExpression teamNameEq = isEmpty(cond.getTeamName()) ? null : qTeam.name.eq(cond.getTeamName());
        BooleanExpression ageGoe = cond.getAgeGoe() == null ? null : qMember.age.goe(cond.getAgeGoe());
        BooleanExpression ageLoe = cond.getAgeLoe() == null ? null : qMember.age.loe(cond.getAgeLoe());


        QueryResults<MemberTeamDto> results = queryFactory
                .select(new QMemberTeamDto(
                        qMember.id,
                        qMember.username,
                        qMember.age,
                        qTeam.id,
                        qTeam.name
                )).from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(userNameEq, teamNameEq, ageGoe, ageLoe)
                .offset(pageable.getOffset())
                .limit(pageable.getPageSize())
                .fetchResults(); // 데이터 내용과 전체 카운트를 한 번에 조회 가능 (실제 쿼리는 2회 전달), 실행 시 필요없는 order by는 제거

        List<MemberTeamDto> content = results.getResults();
        long total = results.getTotal();

        return new PageImpl<>(content, pageable, total);
    }

    @Override
    public Page<MemberTeamDto> searchPageComplex(MemberSearchCondition cond, Pageable pageable) {
        QMember qMember = QMember.member;
        QTeam qTeam = QTeam.team;

        BooleanExpression userNameEq = isEmpty(cond.getUsername()) ? null : qMember.username.eq(cond.getUsername());
        BooleanExpression teamNameEq = isEmpty(cond.getTeamName()) ? null : qTeam.name.eq(cond.getTeamName());
        BooleanExpression ageGoe = cond.getAgeGoe() == null ? null : qMember.age.goe(cond.getAgeGoe());
        BooleanExpression ageLoe = cond.getAgeLoe() == null ? null : qMember.age.loe(cond.getAgeLoe());


        List<MemberTeamDto> content = queryFactory
                .select(new QMemberTeamDto(
                        qMember.id,
                        qMember.username,
                        qMember.age,
                        qTeam.id,
                        qTeam.name
                )).from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(userNameEq, teamNameEq, ageGoe, ageLoe)
                .offset(pageable.getOffset())
                .limit(pageable.getPageSize())
                .fetch(); // 쿼리 분리


//        long total = queryFactory
//                .select(qMember)
//                .from(qMember)
//                .leftJoin(qMember.team, qTeam)
//                .where(userNameEq, teamNameEq, ageGoe, ageLoe)
//                .fetchCount(); // 전체 카운트 조회 (join 회수를 낮출 수 있다)
//          return new PageImpl<>(content, pageable, total);

        JPAQuery<Member> countQuery = queryFactory.select(qMember)
                .from(qMember)
                .leftJoin(qMember.team, qTeam)
                .where(userNameEq, teamNameEq, ageGoe, ageLoe); // count 쿼리 최적화

        return PageableExecutionUtils.getPage(content, pageable, countQuery::fetchCount);
    }
}
