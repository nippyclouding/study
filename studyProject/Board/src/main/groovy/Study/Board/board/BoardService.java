package Study.Board.board;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.Optional;

@Service
@Transactional(readOnly = true)
@RequiredArgsConstructor
public class BoardService {
    private final BoardRepository boardRepository;

    public List<Board> readAll() {
        return boardRepository.findAll();
    }

    @Transactional
    public Board create(Board board) {
        return boardRepository.save(board);
    }

    public Board readDetail(Long boardId) {
        return boardRepository.findById(boardId).orElseThrow(
                () -> new NoSuchElementException("No Board Data")
        );
    }
}
