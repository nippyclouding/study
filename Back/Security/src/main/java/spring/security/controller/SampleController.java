package spring.security.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping("/sample")
@Controller
@Slf4j
public class SampleController {

    // 모든 사람들이 접근 가능한 api
    @GetMapping("/all")
    public void all() {
        log.info("all");
    }

    // 로그인한 회원만 접근 가능한 api
    @GetMapping("/member")
    public void member() {
        log.info("member");
    }

    // 관리자만 접근 가능한 api
    @GetMapping("/admin")
    public void admin() {
        log.info("admin");
    }
}
