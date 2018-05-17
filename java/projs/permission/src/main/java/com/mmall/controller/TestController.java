package com.mmall.controller;

import com.mmall.common.JsonData;
import com.mmall.exception.ParamException;
import com.mmall.exception.PermissionException;
import com.mmall.param.TestVo;
import com.mmall.util.BeanValidator;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections.MapUtils;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Map;


/**
 * Created by bwhite on 18-5-15.
 */
@Controller
@RequestMapping("/test")
@Slf4j
public class TestController {

    @RequestMapping("/hello.json")
    @ResponseBody
    public JsonData hello() {

        log.info("my log works");
        // throw new PermissionException("nimade");
        return JsonData.success("hello permission");

    }

    @RequestMapping("/validate.json")
    @ResponseBody
    public JsonData validate(TestVo vo) throws ParamException {

        log.info("validate");

        BeanValidator.check(vo);

        /*
        try {
            Map<String, String> map = BeanValidator.validateObject(vo);
            if (MapUtils.isEmpty(map)) {
                for (Map.Entry<String, String> entry: map.entrySet()) {
                    log.info("{} -> {}", entry.getKey(), entry.getValue());
                }
            }
        } catch (Exception e) {

        }
        */

        return JsonData.success("hello validate");

    }
}
