package ru.leonidm.webapp.service;

import java.util.HashMap;
import java.util.Map;

public class InMemoryMetricsService implements MetricsService {

    private final Map<String, Long> views = new HashMap<>();

    @Override
    public void incrementView(String link) {
        views.merge(link, 1L, Long::sum);
    }

    @Override
    public long getViews(String link) {
        return views.getOrDefault(link, 0L);
    }
}
