package com.yunhe.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

/**
 * Created by bwhite on 18-5-10.
 */
@Configuration
@EnableWebSecurity
public class SpringSecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private MyUserService myUserService;

    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {

        // 只要能登录即可
        // 基于内存的验证
        // auth.inMemoryAuthentication().withUser("admin").password("111111").roles("ADMIN");
        // auth.inMemoryAuthentication().withUser("demo").password("111111").roles("USER");

        // 用自定义的服务处理权限
        auth.userDetailsService(myUserService).passwordEncoder(new MyPasswordEncoder());


    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                .antMatchers("/").permitAll()
                .anyRequest().authenticated()
                .and()
                .logout().permitAll()
                .and()
                .formLogin();

        http.csrf().disable();
    }

    @Override
    public void configure(WebSecurity web) throws Exception {
        // 忽略路径
        web.ignoring().antMatchers("/js/**", "/css/**", "/images/**");
    }
}
