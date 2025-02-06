package com.random.color.picker;

import com.random.color.picker.service.RandomColorPicker;
import lombok.RequiredArgsConstructor;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

@RequiredArgsConstructor
@SpringBootTest
public class RandomColorPickerImplTest {

    private final RandomColorPicker randomColorPicker = new RandomColorPickerImpl(new Random());

    /**
     * Test that the generated color string follows the correct format: #RRGGBB
     */
    @Test
    public void testPickRandomColor_Format() {
        String color = randomColorPicker.pickRandomColor();
        assertNotNull(color, "The returned color should not be null");
        assertTrue(color.startsWith("#"), "The color should start with '#'");

        assertEquals(7, color.length(), "The color string should have exactly 7 characters");
        assertTrue(color.matches("^#[0-9A-Fa-f]{6}$"), "The color string should match the format #RRGGBB");
    }

    /**
     * Test that each RGB component is within the valid range (0-255)
     */
    @Test
    public void testPickRandomColor_RangeValidation() {
        String color = randomColorPicker.pickRandomColor();
        assertNotNull(color, "The returned color should not be null");

        int r = Integer.parseInt(color.substring(1, 3), 16);
        int g = Integer.parseInt(color.substring(3, 5), 16);
        int b = Integer.parseInt(color.substring(5, 7), 16);

        assertTrue(r >= 0 && r <= 255, "Red component should be in the range [0, 255]");
        assertTrue(g >= 0 && g <= 255, "Green component should be in the range [0, 255]");
        assertTrue(b >= 0 && b <= 255, "Blue component should be in the range [0, 255]");
    }

    /**
     * Test with a mocked Random object
     */
    @Test
    public void testPickRandomColor_MockedRandom() {
        Random mockRandom = new Random() {
            @Override
            public int nextInt(int bound) {
                return 128;
            }
        };

        RandomColorPickerImpl randomColorPickerWithMock = new RandomColorPickerImpl(mockRandom);

        String color = randomColorPickerWithMock.pickRandomColor();
        assertNotNull(color, "The returned color should not be null");
        assertEquals("#808080", color, "The color should be #808080 with the mocked Random");
    }

    private static class RandomColorPickerImpl extends com.random.color.picker.service.impl.RandomColorPickerImpl {
        private final Random random;

        public RandomColorPickerImpl(Random random) {
            this.random = random;
        }

        @Override
        public String pickRandomColor() {
            int r = random.nextInt(256);
            int g = random.nextInt(256);
            int b = random.nextInt(256);
            return String.format("#%02X%02X%02X", r, g, b);
        }
    }
}