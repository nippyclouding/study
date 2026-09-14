package com.example.board.board;

import com.example.board.board.domain.Board;
import com.example.board.board.domain.BoardRequestDto;
import com.example.board.util.EncryptPassword;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import static com.example.board.util.EncryptPassword.encryptSHA256;

@RequiredArgsConstructor
@RequestMapping("/detail")
@RestController
@Slf4j
public class BoardDetailController {

    private final BoardService boardService;

    @GetMapping("/{boardId}")
    public ResponseEntity<?> getDetailBoard(@PathVariable Long boardId) {
        Board board = boardService.getBoardDetail(boardId);

        if (board == null) {
            return ResponseEntity.ok(404);
        }

        return ResponseEntity.ok(board);
    }

    @PostMapping
    public ResponseEntity<?> createBoard(@Validated @ModelAttribute BoardRequestDto dto) {
        if (boardService.createBoard(dto)) {
            return ResponseEntity.ok().build();
        } else return ResponseEntity.status(500).build();
    }

    @PostMapping("/{boardId}/edit")
    public ResponseEntity<?> editBoard(@PathVariable Long boardId, @RequestParam String rawPassword, @Validated @ModelAttribute BoardRequestDto dto) {
        if (boardService.updateBoard(boardId, dto, rawPassword)) {
            return ResponseEntity.ok().build();
        } else return ResponseEntity.status(500).build();
    }

    @PostMapping("/{boardId}/delete")
    public ResponseEntity<?> deleteBoard(@PathVariable Long boardId, @RequestParam String password) {
        boolean isCorrectPassword = boardService.checkPassword(password, boardId);
        if (!isCorrectPassword) {
            return ResponseEntity.status(400).build();
        }

        if (boardService.deleteBoard(boardId)) {
            return ResponseEntity.ok().build();
        } else return ResponseEntity.status(500).build();
    }
}
