package com.random.color.picker.service.impl;

import jakarta.annotation.PostConstruct;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.atomic.AtomicInteger;

@Service
public class VisitService {

    private AtomicInteger visitCounter = new AtomicInteger(0);
    private static final Path VISITS_FILE = Path.of("visits.txt");

    @PostConstruct
    public void init() {
        if (Files.exists(VISITS_FILE)) {
            try {
                String content = Files.readString(VISITS_FILE).trim();
                int count = Integer.parseInt(content);
                visitCounter.set(count);
            } catch (Exception e) {
                // If file reading or parsing fails, default to 0
                visitCounter.set(0);
            }
        }
    }

    public int incrementAndGet() {
        int newCount = visitCounter.incrementAndGet();
        persistCount();
        return newCount;
    }

    public int getCount() {
        return visitCounter.get();
    }

    private void persistCount() {
        try {
            Files.writeString(VISITS_FILE, String.valueOf(visitCounter.get()));
        } catch (IOException e) {
            // Log the error appropriately in production code
            e.printStackTrace();
        }
    }
}
