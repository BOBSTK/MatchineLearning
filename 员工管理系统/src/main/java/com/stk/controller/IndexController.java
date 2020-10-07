package com.stk.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

//templates目录下的所有页面，只能通过controller跳转
//需要模板引擎的支持
@Controller
public class IndexController {
    @RequestMapping("/index")
    public  String index(){
        return "index";
    }
}
