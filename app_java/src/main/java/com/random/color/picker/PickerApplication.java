package com.random.color.picker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "com.random.color.picker")
public class PickerApplication {

	public static void main(String[] args) {
		SpringApplication.run(PickerApplication.class, args);
	}

}
