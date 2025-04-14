package com.example.app_java.service;

import com.example.app_java.dto.Category;
import com.example.app_java.dto.RandomQuoteResponse;
import jakarta.annotation.PostConstruct;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import org.springframework.stereotype.Service;


import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

@Service
public class QuoteService {
    private final List<Category> categories = new ArrayList<>();

    public RandomQuoteResponse getRandomQuote() {
        if (categories.isEmpty()) {
            throw new IllegalStateException("No available categories");
        }

        Random random = new Random();
        Category category = categories.get(random.nextInt(categories.size()));

        if (category.getQuotes().isEmpty()) {
            throw new IllegalStateException("No quotes available in category: " + category.getTitle());
        }

        String quote = category.getQuotes().get(random.nextInt(category.getQuotes().size()));
        return new RandomQuoteResponse(category.getTitle(), quote);
    }


    @PostConstruct
    void initQuotes() {
        try {
            Document doc = Jsoup.connect("https://www.geeksforgeeks.org/famous-quotes/")
                    .userAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...")
                    .timeout(10000)
                    .get();

            Elements quotes = doc.select("li[value]");

            for (var li : quotes) {
                String quoteText = li.text().trim();
                if (!quoteText.isEmpty()) {
                    String[] split = quoteText.split(" - ", 2);
                    String quote = split[0].trim();
                    String author = split.length > 1 ? split[1].trim() : "Unknown author";

                    Category category = new Category();
                    category.setTitle(author);
                    category.setQuotes(List.of(quote));
                    categories.add(category);
                }
            }

            if (categories.isEmpty()) {
                Category defaultCategory = new Category();
                defaultCategory.setTitle("Test Category");
                defaultCategory.setQuotes(List.of("This is a test quote"));
                categories.add(defaultCategory);
            }

        } catch (IOException e) {
            System.err.println("Connection error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Parsing error: " + e.getMessage());
        }
    }

}
