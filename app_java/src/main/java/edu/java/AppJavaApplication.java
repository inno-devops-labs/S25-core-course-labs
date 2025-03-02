package edu.java;

import edu.java.configuration.ApplicationConfiguration;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;

@SpringBootApplication
@EnableConfigurationProperties(ApplicationConfiguration.class)
public class AppJavaApplication {
    public static void main(String[] args) {
        SpringApplication.run(AppJavaApplication.class, args);
    }
}
