package shinhanproject.sh.ex3.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import shinhanproject.sh.ex3.dto.PageRequestDto;
import shinhanproject.sh.ex3.service.BoardService;

@Controller
@RequestMapping("/board/")
@RequiredArgsConstructor
public class BoardController {
    private final BoardService boardService;

    @GetMapping("/list")
    public void list(PageRequestDto dto, Model model) {
        model.addAttribute("result", boardService.getList(dto));
    }
}
