package ru.leonidm.webapp.service;

import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class RandomGeneratorService implements GeneratorService {

    private final List<Character> availableChars;

    public RandomGeneratorService(List<Character> availableChars) {
        if (availableChars.isEmpty()) {
            throw new IllegalArgumentException("There must be at least one available char");
        }

        this.availableChars = availableChars;
    }

    @Override
    public String generatePassword(int length) {
        ThreadLocalRandom random = ThreadLocalRandom.current();

        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < length; i++) {
            char chr = availableChars.get(random.nextInt(availableChars.size()));
            stringBuilder.append(chr);
        }

        return stringBuilder.toString();
    }

}
