/**
 * This package contains service interfaces.
 */
package com.random.color.picker.service;

import org.springframework.stereotype.Service;

/**
 * Interface segregation
 */
@Service
public interface RandomColorPicker {
    String pickRandomColor();
}
