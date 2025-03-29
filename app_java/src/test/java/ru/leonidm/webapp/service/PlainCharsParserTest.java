package ru.leonidm.webapp.service;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import java.util.List;

class PlainCharsParserTest {

    @Test
    void parseCharsTest() {
        PlainCharsParser parser = new PlainCharsParser();

        List<Character> characters = parser.parseChars("abcdef-01$5%\\");
        assertEquals(List.of('a', 'b', 'c', 'd', 'e', 'f', '-', '0', '1', '$', '5', '%', '\\'), characters);
    }
}
