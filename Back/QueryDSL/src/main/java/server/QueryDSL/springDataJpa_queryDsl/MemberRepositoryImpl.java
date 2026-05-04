package server.QueryDSL.springDataJpa_queryDsl;

import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import jakarta.persistence.EntityManager;
import server.QueryDSL.entity.QMember;
import server.QueryDSL.entity.QTeam;

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
}
