package shinhanproject.sh.ex2.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import shinhanproject.sh.ex2.dto.GuestBookDto;
import shinhanproject.sh.ex2.dto.PageRequestDto;
import shinhanproject.sh.ex2.service.GuestBookService;

@Controller
@RequestMapping("/guestBook")
@RequiredArgsConstructor
@Slf4j
public class GuestBookController {

    private final GuestBookService guestBookService;

    @GetMapping("/")
    public String index() {
        return "redirect:/guestBook/list";
    }

    @GetMapping("/list")
    public void list(PageRequestDto dto, Model model) {
        log.info("list....");
        model.addAttribute("result", guestBookService.getList(dto));
    }

    @GetMapping("/register")
    public void register() {
        log.info("register GET....");
    }

    @PostMapping("/register")
    public String registerPost(GuestBookDto dto, RedirectAttributes attributes) {
        log.info("register POST....");
        Long id = guestBookService.register(dto);
        attributes.addFlashAttribute("msg", id);
        return "redirect:/guestBook/list";
    }
}
