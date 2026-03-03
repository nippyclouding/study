package shinhanproject.sh.ex3.repository;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import shinhanproject.sh.ex3.domain.Board;

import java.util.List;

public interface BoardRepository extends JpaRepository<Board, Long> {
    @Query("select b, w from Board b left join b.writer w where b.bno =:bno")
    Object[] getBoardWithWriter(@Param("bno") Long bno);

    @Query("select b, r FROM Board b LEFT JOIN Reply r ON r.board = b WHERE b.bno = :bno")
    List<Object[]> getBoardWithReply(@Param("bno") Long bno);

    // 1. 목록 조회 (페이징)
    @Query(value = "SELECT b, w, count(r) " +
            " FROM Board b " +
            " LEFT JOIN b.writer w " +
            " LEFT JOIN Reply r ON r.board = b " +
            " GROUP BY b",
            countQuery = "SELECT COUNT(b) FROM Board b")
    Page<Object[]> getBoardWithReply(Pageable pageable);

    // 2. 특정 게시글 상세 조회 (단건)
    @Query("SELECT b, w, count(r) " +
            " FROM Board b " +
            " LEFT JOIN b.writer w " +
            " LEFT JOIN Reply r ON r.board = b " +
            " WHERE b.bno = :bno")
    Object[] getBoardByBno(@Param("bno") Long bno);
}
