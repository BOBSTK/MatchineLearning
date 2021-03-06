package com.stk.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class MyMVCConfig implements WebMvcConfigurer {
    //视图跳转
    @Override

    public void addViewControllers(ViewControllerRegistry registry) {
        //一般用来配置首页
        registry.addViewController("/").setViewName("index");
        registry.addViewController("/index.html").setViewName("index");
        registry.addViewController("/main.html").setViewName("dashboard"); //main.html是虚拟的，用来重定向，隐藏用户请求信息
    }
}
