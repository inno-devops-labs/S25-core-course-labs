package ru.leonidm.webapp.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import ru.leonidm.webapp.service.GeneratorService;
import ru.leonidm.webapp.service.MetricsService;

@RestController
@AllArgsConstructor
public class WebAppController {

    private final MetricsService metricsService;
    private final GeneratorService generatorService;

    @GetMapping("/")
    public String index() {
        metricsService.incrementView("/");
        return "<div><h1>Total views of this page: %d</h1><a href=\"/password\">Generate random password</a></div>"
                .formatted(metricsService.getViews("/"));
    }

    @GetMapping("/password")
    public String password() {
        metricsService.incrementView("/password");
        return "<div><h1>Total views of this page: %d</h1><p>Generated password: <b>%s</b></p></div>"
                .formatted(metricsService.getViews("/password"), generatorService.generatePassword(16));
    }

}
