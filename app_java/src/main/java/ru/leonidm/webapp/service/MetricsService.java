package ru.leonidm.webapp.service;

public interface MetricsService {

    void incrementView(String link);

    long getViews(String link);

}
