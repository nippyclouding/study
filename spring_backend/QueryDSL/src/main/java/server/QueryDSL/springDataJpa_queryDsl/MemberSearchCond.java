package server.QueryDSL.springDataJpa_queryDsl;

import lombok.Data;

@Data
public class MemberSearchCond {
    private String username;
    private String teamName;
    private Integer ageGoe; // greater or equal
    private Integer ageLoe; // less or equal
}
