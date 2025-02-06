package ru.leonidm.webapp.configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import ru.leonidm.webapp.service.CharsParser;
import ru.leonidm.webapp.service.GeneratorService;
import ru.leonidm.webapp.service.InMemoryMetricsService;
import ru.leonidm.webapp.service.MetricsService;
import ru.leonidm.webapp.service.RandomGeneratorService;
import ru.leonidm.webapp.service.RangedCharsParser;

@Configuration
public class WebAppConfiguration {

    @Bean
    public MetricsService metricsService() {
        return new InMemoryMetricsService();
    }

    @Bean
    public CharsParser charsParser() {
        return new RangedCharsParser();
    }

    @Bean
    public GeneratorService generatorService(@Value("${webapp.generator.chars}") String chars,
                                             CharsParser charsParser) {
        return new RandomGeneratorService(charsParser.parseChars(chars));
    }
}
