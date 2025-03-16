package com.random.color.picker.controller;

import com.random.color.picker.service.RandomColorPicker;
import com.random.color.picker.service.impl.VisitService;
import io.micrometer.core.instrument.Counter;
import io.micrometer.core.instrument.MeterRegistry;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/hex")
@RequiredArgsConstructor
public class RandomHexController {

    private final RandomColorPicker randomColorPicker;
    private final MeterRegistry meterRegistry;
    private final VisitService visitService;

    private Counter colorRequestCounter;

    @GetMapping(value = "/color")
    public String getRandomHex(Model thymeLeafEnt) {

        if (colorRequestCounter == null) {
            colorRequestCounter = Counter.builder("random_hex_controller_requests_total")
                    .description("Total number of requests to the /hex/color endpoint")
                    .register(meterRegistry);
        }
        colorRequestCounter.increment();

        visitService.incrementAndGet();

        thymeLeafEnt.addAttribute("color", randomColorPicker.pickRandomColor());
        return "random-color";
    }
}
