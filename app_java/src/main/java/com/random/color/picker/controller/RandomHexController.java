package com.random.color.picker.controller;

import com.random.color.picker.service.RandomColorPicker;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 * Controller for generating random hexadecimal colors.
 */
@Controller
@RequestMapping("/hex")
@RequiredArgsConstructor
public final class RandomHexController {

    private final RandomColorPicker randomColorPicker;

    /**
     * Handles GET requests to generate a random hexadecimal color.
     *
     * @param thymeLeafEnt The Thymeleaf model object.
     * @return A view with the generated color.
     */
    @GetMapping(value = "/color")
    public String getRandomHex(final Model thymeLeafEnt) {
        thymeLeafEnt.addAttribute("color", randomColorPicker.pickRandomColor());
        return "random-color";
    }
}