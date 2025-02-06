package ru.leonidm.webapp.service;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class InMemoryMetricsServiceTest {

    @Test
    void serviceTest() {
        InMemoryMetricsService service = new InMemoryMetricsService();
        String link = "/";

        for (int i = 0; i < 100; i++) {
            long views = service.getViews(link);
            assertEquals(i, views);

            service.incrementView(link);
        }
    }

}
