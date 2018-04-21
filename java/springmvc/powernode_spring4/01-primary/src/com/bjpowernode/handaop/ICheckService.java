package com.bjpowernode.handaop;

/**
 * Created by bwhite on 18-4-21.
 * 主业务接口
 */
public interface ICheckService {
    boolean check(String username, String password) throws UserException;
}
