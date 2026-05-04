package server.QueryDSL.springDataJpa_queryDsl;

import java.util.List;

public interface MemberRepositoryCustom {
    List<MemberTeamDto> search(MemberSearchCond cond);
}
