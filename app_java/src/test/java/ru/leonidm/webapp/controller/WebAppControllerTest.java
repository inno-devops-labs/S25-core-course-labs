package ru.leonidm.webapp.controller;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.Test;
import ru.leonidm.webapp.service.GeneratorService;
import ru.leonidm.webapp.service.MetricsService;

class WebAppControllerTest {

    @Test
    void indexTest() {
        MetricsService metricsService = mock(MetricsService.class);
        GeneratorService generatorService = mock(GeneratorService.class);

        long views = 273920L;
        when(metricsService.getViews("/")).thenReturn(views);

        WebAppController controller = new WebAppController(metricsService, generatorService);
        String response = controller.index();
        assertTrue(response.contains(String.valueOf(views)));

        verify(metricsService, times(1)).incrementView("/");
        verify(metricsService, times(1)).getViews("/");
        verify(generatorService, times(0)).generatePassword(16);
    }

    @Test
    void passwordTest() {
        MetricsService metricsService = mock(MetricsService.class);
        GeneratorService generatorService = mock(GeneratorService.class);

        long views = 851829L;
        String password = "$generatedpassword$";
        when(metricsService.getViews("/password")).thenReturn(views);
        when(generatorService.generatePassword(16)).thenReturn(password);

        WebAppController controller = new WebAppController(metricsService, generatorService);
        String response = controller.password();
        assertTrue(response.contains(String.valueOf(views)));
        assertTrue(response.contains(password));

        verify(metricsService, times(1)).incrementView("/password");
        verify(metricsService, times(1)).getViews("/password");
        verify(generatorService, times(1)).generatePassword(16);
    }

}
