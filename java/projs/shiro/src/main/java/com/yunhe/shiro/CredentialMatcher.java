package com.yunhe.shiro;

import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.authc.credential.SimpleCredentialsMatcher;

/**
 * Created by bwhite on 18-5-11.
 * 重写密码校验规则
 *
 * 这些自定义的内容都要注入到 shiro 的配置中, 需要定义一个 shiro 的配置类 ShiroConfiguration
 */
public class CredentialMatcher extends SimpleCredentialsMatcher {

    @Override
    public boolean doCredentialsMatch(AuthenticationToken token, AuthenticationInfo info) {
        UsernamePasswordToken usernamePasswordToken = (UsernamePasswordToken)token;
        String password = new String(usernamePasswordToken.getPassword());
        String dbPassword = (String)info.getCredentials();
        return this.equals(password, dbPassword);
    }
}
