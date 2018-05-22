package com.mmall.common;

import com.mmall.util.JsonMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.handler.HandlerInterceptorAdapter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Map;

/**
 * Created by bwhite on 18-5-17.
 * 全局的
 */
@Slf4j
public class HttpInterceptor extends HandlerInterceptorAdapter {

    private static final String START_TIME = "requestStartTime";

    // 请求之前
    // 可能会用来输出参数
    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {

        String url = request.getRequestURI().toString();
        Map parameterMap = request.getParameterMap();
        log.info("request start - url:{}, params:{}", url, JsonMapper.obj2String(parameterMap));
        long start = System.currentTimeMillis();
        request.setAttribute(START_TIME, start);
        return true;
    }

    // 请求正常结束时
    // 监控接口的处理时间
    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {
        String url = request.getRequestURI().toString();
        Map parameterMap = request.getParameterMap();
        long start = (long)request.getAttribute(START_TIME);
        long end = System.currentTimeMillis();
//        log.info("request - finish - url:{}, time_cost:{}", url, JsonMapper.obj2String(parameterMap));
        log.info("request - finish - url:{}, time_cost:{}", url, end - start);

        removeThreadLocalInfo();
    }

    // 所有请求结束时
    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {
        String url = request.getRequestURI().toString();
        Map parameterMap = request.getParameterMap();
        log.info("request - complete - url:{}, params:{}", url, JsonMapper.obj2String(parameterMap));

        removeThreadLocalInfo();
    }

    public void removeThreadLocalInfo() {
        RequestHolder.remove();;
    }
}
