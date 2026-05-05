package server.QueryDSL.naturalJpa_queryDsl;

import lombok.Data;

@Data
public class MemberSearchCondition {
    // 검색 조건 : 회원명, 팀명, 나이
    private String username;
    private String teamName;
    private Integer ageGoe;
    private Integer ageLoe;
}
