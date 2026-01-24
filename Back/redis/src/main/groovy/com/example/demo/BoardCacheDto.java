package com.example.demo;

import java.time.LocalDateTime;

public record BoardCacheDto(
        Long id,
        String title,
        LocalDateTime createdAt
) {}