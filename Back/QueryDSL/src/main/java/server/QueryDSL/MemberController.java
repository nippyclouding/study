package server.QueryDSL;

import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RestController;
import server.QueryDSL.naturalJpa_queryDsl.MemberJpaRepository;
import server.QueryDSL.naturalJpa_queryDsl.MemberSearchCondition;
import server.QueryDSL.naturalJpa_queryDsl.MemberTeamDto;
import server.QueryDSL.springDataJpa_queryDsl.MemberRepository;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class MemberController {
    private final MemberJpaRepository memberJpaRepository;
    private final MemberRepository memberRepository;

    @GetMapping("/v1/members")
    public List<MemberTeamDto> searchMemberV1(@ModelAttribute MemberSearchCondition cond) {
        return memberJpaRepository.search(cond);
        // http://localhost:8080/v1/members?teamName=teamB&ageGoe=31&ageLoe=35
    }
    
    @GetMapping("/v2/members")
    public Page<server.QueryDSL.springDataJpa_queryDsl.MemberTeamDto> searchMemberV2(@ModelAttribute MemberSearchCondition cond, Pageable pageable) {
        return memberRepository.searchPageSimple(cond, pageable);
        // http://localhost:8080/v2/members?size=5&page=2
    }
    
    @GetMapping("/v3/members")
    public Page<server.QueryDSL.springDataJpa_queryDsl.MemberTeamDto> searchMemberV3(@ModelAttribute MemberSearchCondition cond, Pageable pageable) {
        return memberRepository.searchPageComplex(cond, pageable);
    }
}
