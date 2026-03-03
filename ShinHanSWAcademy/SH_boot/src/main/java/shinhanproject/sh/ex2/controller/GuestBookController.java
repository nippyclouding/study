package shinhanproject.sh.ex2.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import shinhanproject.sh.ex2.dto.PageRequestDto;
import shinhanproject.sh.ex2.service.GuestBookService;

@Controller
@RequestMapping("/guestBook")
@RequiredArgsConstructor
@Slf4j
public class GuestBookController {

    private final GuestBookService guestBookService;

    @GetMapping("/")
    public String list() {
        log.info("list....");
        return "guestBook/list";
    }

    @GetMapping("/list")
    public void list(PageRequestDto dto, Model model) {
        model.addAttribute("result", guestBookService.getList(dto));
    }
}
