package ru.leonidm.webapp.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrowsExactly;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

import java.util.List;

class RangedCharsParserTest {

    @Test
    void rangedCharsTest() {
        RangedCharsParser parser = new RangedCharsParser();

        List<Character> characters = parser.parseChars("a-\\d0\\-9\\\\");
        assertEquals(List.of('a', 'b', 'c', 'd', '0', '-', '9', '\\'), characters);

        IllegalArgumentException exception = assertThrowsExactly(IllegalArgumentException.class, () -> parser.parseChars("0-"));
        assertTrue(exception.getMessage().contains("dash"));

        exception = assertThrowsExactly(IllegalArgumentException.class, () -> parser.parseChars("0--"));
        assertTrue(exception.getMessage().contains("dashes"));

        exception = assertThrowsExactly(IllegalArgumentException.class, () -> parser.parseChars("a\\"));
        assertTrue(exception.getMessage().contains("backslash"));
    }
}
