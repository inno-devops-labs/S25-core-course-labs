package com.example.app_java.controller;

import com.example.app_java.dto.RandomQuoteResponse;
import com.example.app_java.service.QuoteService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.springframework.http.ResponseEntity;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

class QuoteControllerTest {

    @Mock
    private QuoteService quoteService;

    private QuoteController quoteController;

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        quoteController = new QuoteController(quoteService);
    }

    @Test
    void getRandomQuoteHtml_shouldReturnValidHtmlResponse() {
        RandomQuoteResponse mockQuote = new RandomQuoteResponse("Author", "This is a random quote.");
        when(quoteService.getRandomQuote()).thenReturn(mockQuote);

        ResponseEntity<String> response = quoteController.getRandomQuoteHtml();

        String expectedHtml = "<!DOCTYPE html>" +
                "<html>" +
                "<head><title>Random Quote</title></head>" +
                "<body>" +
                "<h1>Random Quote</h1>" +
                "<p><strong>Author:</strong> Author</p>" +
                "<p><strong>Quote:</strong> This is a random quote.</p>" +
                "</body>" +
                "</html>";
        assertEquals(200, response.getStatusCodeValue());
        assertEquals("text/html", response.getHeaders().getContentType().toString());
        assertEquals(expectedHtml, response.getBody());
    }
}