package com.bjpowernode.handaop;

/**
 * Created by bwhite on 18-4-21.
 * 目标类
 */
public class CheckServiceImpl implements ICheckService {

    // 目标方法
    @Override
    public boolean check(String username, String password) throws UserException {
//        if (!"mima".equals(username) || !"123".equals(password)) {
//            throw new UserException();
//        }
        if (!"mima".equals(username)) {
            throw new UserNameException("username error");
        }
        if (!"123".equals(password)) {
            throw new PasswordException("password error");
        }

        return true;
    }
}
