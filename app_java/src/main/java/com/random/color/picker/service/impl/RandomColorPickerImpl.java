package com.random.color.picker.service.impl;

import com.random.color.picker.service.RandomColorPicker;
import org.springframework.stereotype.Service;

import java.util.Random;

@Service
public class RandomColorPickerImpl implements RandomColorPicker {
    @Override
    public String pickRandomColor() {
        Random random = new Random();
        int r = random.nextInt(256);
        int g = random.nextInt(256);
        int b = random.nextInt(256);
        return String.format("#%02X%02X%02X", r, g, b);
    }
}
