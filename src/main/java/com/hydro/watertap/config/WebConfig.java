package com.hydro.watertap.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.http.CacheControl;
import org.springframework.http.MediaType;
import org.springframework.web.reactive.function.server.*;

@Configuration
public class WebConfig {

    @Bean
    public RouterFunction<ServerResponse> spaRouter() {

        return RouterFunctions
                .resources("/**", new ClassPathResource("static/")) // servir archivos estáticos
                .andRoute(
                        RequestPredicates.GET("/**")
                                .and(RequestPredicates.accept(MediaType.TEXT_HTML)),
                        request -> ServerResponse.ok()
                                .cacheControl(CacheControl.noCache())
                                .contentType(MediaType.TEXT_HTML)
                                .bodyValue(new ClassPathResource("static/index.html"))
                );
    }
}
