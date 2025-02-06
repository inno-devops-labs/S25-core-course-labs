package com.example.mgntime;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(ClockController.class)
public class ClockControllerTest {

	@Autowired
	private MockMvc mockMvc;

	@Test
	public void testGetTime() throws Exception {
		mockMvc.perform(get("/time"))
				.andExpect(status().isOk())
				.andExpect(content().string(org.hamcrest.Matchers.matchesPattern("\\d{2}:\\d{2}:\\d{2}")));
	}
}
