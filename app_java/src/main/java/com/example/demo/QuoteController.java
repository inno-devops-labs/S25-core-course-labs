package com.example.demo;

import java.util.List;
import java.util.Map;
import java.util.Random;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class QuoteController {

    @GetMapping("/")
    public String getRandomQuote(Model model) {
        Map<String, List<String>> quotesByAlbum = Map.of(
                "1989", List.of(
                        "Cause darling I'm a nightmare dressed like a daydream.",
                        "Saw you there and I thought oh my god, look at that face, you look like my next mistake!"),
                "Red", List.of(
                        "The idea you had of me, who was she?",
                        "It's supposed to be fun turning twenty-one",
                        "I'm a soldier who's returning half her weight",
                        "You tell me about your past thinking your future was me.",
                        "And I forget about you long enough to forget why I needed to."));

        Map<String, String> albumImages = Map.of(
                "Red", "/images/Red.jpg",
                "1989", "/images/1989.jpg");

        Random random = new Random();
        List<String> albums = List.copyOf(quotesByAlbum.keySet());
        String randomAlbum = albums.get(random.nextInt(albums.size()));

        List<String> quotes = quotesByAlbum.get(randomAlbum);
        String randomQuote = quotes.get(random.nextInt(quotes.size()));

        model.addAttribute("quote", randomQuote);
        model.addAttribute("album", randomAlbum);
        model.addAttribute("image", albumImages.get(randomAlbum));

        return "quote";
    }
}
