package server.QueryDSL.springDataJpa_queryDsl;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import server.QueryDSL.naturalJpa_queryDsl.MemberSearchCondition;

import java.util.List;

public interface MemberRepositoryCustom {
    List<MemberTeamDto> search(MemberSearchCond cond);

    // queryDsl + springData Jpa
    Page<MemberTeamDto> searchPageSimple(MemberSearchCondition cond, Pageable pageable);
    Page<MemberTeamDto> searchPageComplex(MemberSearchCondition cond, Pageable pageable);
}

