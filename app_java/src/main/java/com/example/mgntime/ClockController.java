package com.example.mgntime;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

@Controller
public class ClockController {

	@GetMapping("/")
	public String getCurrentTime(Model model) {
		// Get the current time in Magnitogorsk (Asia/Yekaterinburg timezone)
		ZonedDateTime now = ZonedDateTime.now(ZoneId.of("Asia/Yekaterinburg"));
		String formattedTime = now.format(DateTimeFormatter.ofPattern("HH:mm:ss"));

		// Add the time to the model
		model.addAttribute("currentTime", formattedTime);
		return "index";
	}

	@GetMapping("/time")
	@ResponseBody
	public String getTime() {
		// Get the current time in Magnitogorsk (Asia/Yekaterinburg timezone)
		ZonedDateTime now = ZonedDateTime.now(ZoneId.of("Asia/Yekaterinburg"));
		return now.format(DateTimeFormatter.ofPattern("HH:mm:ss"));
	}
}