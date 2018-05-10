package com.yunhe.shiro.service;

import com.yunhe.shiro.model.User;

/**
 * Created by bwhite on 18-5-10.
 */
public interface UserService {

    User findByUsername(String username);
}
