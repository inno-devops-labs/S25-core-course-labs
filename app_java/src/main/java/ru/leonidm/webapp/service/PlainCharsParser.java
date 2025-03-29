package ru.leonidm.webapp.service;

import java.util.List;

public class PlainCharsParser implements CharsParser {

    @Override
    public List<Character> parseChars(String chars) {
        return chars.chars()
                .mapToObj(i -> (char) i)
                .toList();
    }
}
