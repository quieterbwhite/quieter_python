package com.yunhe.shiro.mapper;

import com.yunhe.shiro.model.User;
import org.apache.ibatis.annotations.Param;

/**
 * Created by bwhite on 18-5-10.
 */
public interface UserMapper {

    User findByUsername(@Param("username") String username);
}
