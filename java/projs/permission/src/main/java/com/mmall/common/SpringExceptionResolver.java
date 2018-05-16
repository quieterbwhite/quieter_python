package com.mmall.common;

import com.mmall.exception.PermissionException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.servlet.HandlerExceptionResolver;
import org.springframework.web.servlet.ModelAndView;

/**
 * Created by bwhite on 18-5-16.
 * 需要配置来使其被 spring 管理
 */
public class SpringExceptionResolver implements HandlerExceptionResolver {

    @Override
    public ModelAndView resolveException(javax.servlet.http.HttpServletRequest httpServletRequest, javax.servlet.http.HttpServletResponse httpServletResponse, Object o, Exception e) {

        String url = httpServletRequest.getRequestURL().toString();
        ModelAndView mv;
        String defaultMsg = "system error";

        // .json .page
        // 这里要求项目中所有请求json数据的都使用 .json 结尾
        if (url.endsWith(".json")) {
            if (e instanceof PermissionException) {
                JsonData result = JsonData.fail(e.getMessage());
                // 使用 spring-servlet.xml 中配置的 jsonView 来处理
                mv = new ModelAndView("jsonView", result.toMap());
            } else {
                JsonData result = JsonData.fail(defaultMsg);
                mv = new ModelAndView("jsonView", result.toMap());
            }
        } else if (url.endsWith(".page")){ // 这里要求项目中所有请求page数据的都使用 .page 结尾
            JsonData result = JsonData.fail(defaultMsg);
            // 自动读取 exception.jsp 文件并返回
            mv = new ModelAndView("exception", result.toMap());
        } else {
            JsonData result = JsonData.fail(defaultMsg);
            mv = new ModelAndView("jsonView", result.toMap());
        }

        return mv;

    }
}
