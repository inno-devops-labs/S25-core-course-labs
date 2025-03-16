package com.random.color.picker.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.random.color.picker.service.impl.VisitService;

@RestController
public class VisitController {

    private final VisitService visitService;

    public VisitController(VisitService visitService) {
        this.visitService = visitService;
    }

    @GetMapping("/visits")
    public String getVisits() {
        int count = visitService.getCount();
        return "Visits: " + count;
    }
}
