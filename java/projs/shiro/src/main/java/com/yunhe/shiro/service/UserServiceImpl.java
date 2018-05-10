package com.yunhe.shiro.service;

import com.yunhe.shiro.mapper.UserMapper;
import com.yunhe.shiro.model.User;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

/**
 * Created by bwhite on 18-5-10.
 */
@Service
public class UserServiceImpl implements UserService {

    @Resource
    private UserMapper userMapper;

    @Override
    public User findByUsername(String username) {
        return userMapper.findByUsername(username);
    }
}
