package com.example.app_java.controller;

import com.example.app_java.dto.RandomQuoteResponse;
import com.example.app_java.service.QuoteService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/quotes")
public class QuoteController {
    private final QuoteService quoteService;

    public QuoteController(QuoteService quoteService) {
        this.quoteService = quoteService;
    }

    @GetMapping("/random")
    public ResponseEntity<String> getRandomQuoteHtml() {
        RandomQuoteResponse randomQuote = quoteService.getRandomQuote();
        String html = "<!DOCTYPE html>" +
                "<html>" +
                "<head><title>Random Quote</title></head>" +
                "<body>" +
                "<h1>Random Quote</h1>" +
                "<p><strong>Author:</strong> " + randomQuote.getCategory() + "</p>" +
                "<p><strong>Quote:</strong> " + randomQuote.getQuote() + "</p>" +
                "</body>" +
                "</html>";

        return ResponseEntity.ok()
                .header("Content-Type", "text/html")
                .body(html);
    }

}
