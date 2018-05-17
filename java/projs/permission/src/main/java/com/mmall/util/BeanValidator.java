package com.mmall.util;

import com.google.common.base.Preconditions;
import com.google.common.collect.Lists;
import com.google.common.collect.Maps;
import com.mmall.exception.ParamException;
import org.apache.commons.collections.MapUtils;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import javax.validation.ValidatorFactory;
import java.util.*;

/**
 * Created by bwhite on 18-5-17.
 */
public class BeanValidator {

    // 全局的校验工厂
    private static ValidatorFactory validatorFactory = Validation.buildDefaultValidatorFactory();

    // 普通的校验方法
    // <T> 代表传入的类型，可以传入很多种类型
    // Map<String, String>, 返回值，<字段，错误信息>
    public static <T> Map<String, String> validate(T t, Class... groups) {
        // 获得一个验证器
        Validator validator = validatorFactory.getValidator();
        Set validateResult = validator.validate(t, groups);

        if (validateResult.isEmpty()) {
            return Collections.emptyMap();
        } else {
            LinkedHashMap errors = Maps.newLinkedHashMap();
            Iterator iterator = validateResult.iterator();
            while (iterator.hasNext()) {
                ConstraintViolation violation = (ConstraintViolation)iterator.next();
                errors.put(violation.getPropertyPath().toString(), violation.getMessage());
            }
            return errors;
        }
    }

    public static Map<String, String> validateList(Collection<?> collection) {

        Preconditions.checkNotNull(collection);

        Iterator iterator = collection.iterator();
        Map errors;

        do {
            if (!iterator.hasNext()) {
                return Collections.emptyMap();
            }
            Object object = iterator.next();
            errors = validate(object, new Class[0]);  // new Class[0] 占位, 符合函数调用
        } while (errors.isEmpty());

        return errors;
    }

    public static Map<String, String> validateObject(Object first, Object... objects) {

        if (objects != null && objects.length > 0) {
            return validateList(Lists.asList(first, objects));
        } else {
            return validate(first, new Class[0]);
        }
    }

    public static void check(Object object) throws ParamException {
        Map<String, String> map = BeanValidator.validateObject(object);
        if (MapUtils.isEmpty(map)) {
            throw new ParamException(map.toString());
        }
    }


}
