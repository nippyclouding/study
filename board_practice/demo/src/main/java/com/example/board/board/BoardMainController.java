package com.example.board.board;

import com.example.board.board.domain.Board;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequiredArgsConstructor
@RequestMapping("/main")
@RestController
@Slf4j
public class BoardMainController {

    private final BoardService boardService;

    @GetMapping
    public ResponseEntity<?> getMainPage(@RequestParam(defaultValue = "0") int currentPage) {
        List<Board> boards = boardService.getMainBoardsByPaging(currentPage);
        return ResponseEntity.ok(boards);
    }

    @GetMapping("/count")
    public ResponseEntity<?> getTotalCount() {
        int totalCount = boardService.getCount();
        return ResponseEntity.ok(totalCount);
    }
}
