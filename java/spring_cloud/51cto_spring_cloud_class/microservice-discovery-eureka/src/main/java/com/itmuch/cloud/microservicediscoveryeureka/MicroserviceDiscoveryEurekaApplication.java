package com.itmuch.cloud.microservicediscoveryeureka;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@EnableEurekaServer
public class MicroserviceDiscoveryEurekaApplication {

	public static void main(String[] args) {
		SpringApplication.run(MicroserviceDiscoveryEurekaApplication.class, args);
	}
}
