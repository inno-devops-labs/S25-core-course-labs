package ru.leonidm.webapp.service;

import java.util.ArrayList;
import java.util.List;

public class RangedCharsParser implements CharsParser {

    @Override
    public List<Character> parseChars(String chars) {
        List<Character> characters = new ArrayList<>();

        if (!chars.isEmpty() && chars.charAt(0) == '-') {
            throw new IllegalArgumentException("Invalid formated chars: dash at the start of the string");
        }

        for (int i = 0; i < chars.length(); i++) {
            char chr = chars.charAt(i);
            if (chr == '\\') {
                i++;
                if (i >= chars.length()) {
                    throw new IllegalArgumentException("Invalid formated chars: single backslash at the end of the string");
                }

                chr = chars.charAt(i);
            }

            if (i + 1 < chars.length()) {
                char next = chars.charAt(i + 1);
                if (next == '-') {
                    i += 2;
                    if (i >= chars.length()) {
                        throw new IllegalArgumentException("Invalid formated chars: dash at the end of the string");
                    }

                    char to = chars.charAt(i);
                    if (to == '-') {
                        throw new IllegalArgumentException("Invalid formated chars: two dashes in a row");
                    } else if (to == '\\') {
                        i++;
                        if (i >= chars.length()) {
                            throw new IllegalArgumentException("Invalid formated chars: single backslash at the end of the string");
                        }

                        to = chars.charAt(i);
                    }

                    for (char j = chr; j <= to; j++) {
                        characters.add(j);
                    }
                } else {
                    characters.add(chr);
                }
            } else {
                characters.add(chr);
            }
        }

        return characters;
    }
}
