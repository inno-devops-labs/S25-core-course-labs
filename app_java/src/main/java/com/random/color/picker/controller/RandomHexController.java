package com.random.color.picker.controller;

import com.random.color.picker.service.RandomColorPicker;
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

    @GetMapping(value = "/color")
    public String getRandomHex(Model thymeLeafEnt) {
        thymeLeafEnt.addAttribute("color", randomColorPicker.pickRandomColor());
        return "random-color";
    }
}
