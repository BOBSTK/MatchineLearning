package com.stk.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.thymeleaf.util.StringUtils;

@Controller
public class LoginController {
    @RequestMapping("/user/login")
    //@ResponseBody
    public String Login(@RequestParam("username") String username, @RequestParam("password") String password, Model model){
        //具体的业务
        if(!StringUtils.isEmpty(username) && "123456".equals(password)){
            return "redirect:/main.html"; //重定向
        }else{
            //登录失败
            model.addAttribute("msg","用户名或密码错误");
            return "index";
        }
    }
}
