package com.mmall.service;

import com.google.common.base.Preconditions;
import com.mmall.beans.PageQuery;
import com.mmall.beans.PageResult;
import com.mmall.dao.SysUserMapper;
import com.mmall.exception.ParamException;
import com.mmall.model.SysUser;
import com.mmall.param.UserParam;
import com.mmall.util.BeanValidator;
import com.mmall.util.MD5Util;
import com.mmall.util.PasswordUtil;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.Date;
import java.util.List;

/**
 * Created by bwhite on 18-5-21.
 */
@Service
public class SysUserService {

    @Resource
    private SysUserMapper sysUserMapper;

    public void save(UserParam param) {

        BeanValidator.check(param);

        if (checkTelephoneExists(param.getTelephone(), param.getId())) {
            throw new ParamException("电话已被占用");
        }
        if (checkEmailExists(param.getMail(), param.getId())) {
            throw new ParamException("邮箱已被占用");
        }

        String password = PasswordUtil.randomPassword();

        password = "111111";

        String encryptedPassword = MD5Util.encrypt(password);

        SysUser user = SysUser.builder()
                .username(param.getUsername())
                .telephone(param.getTelephone())
                .mail(param.getMail())
                .password(encryptedPassword)
                .deptId(param.getDeptId())
                .status(param.getStatus())
                .remark(param.getRemark())
                .build();
        user.setOperator("system");
        user.setOperateTime(new Date());
        user.setOperateId("127.0.0.1");

        // TODO send email

        sysUserMapper.insert(user);
    }

    public void update(UserParam param) {
        BeanValidator.check(param);
        if(checkTelephoneExists(param.getTelephone(), param.getId())) {
            throw new ParamException("电话已被占用");
        }
        if(checkEmailExists(param.getMail(), param.getId())) {
            throw new ParamException("邮箱已被占用");
        }
        SysUser before = sysUserMapper.selectByPrimaryKey(param.getId());
        Preconditions.checkNotNull(before, "待更新的用户不存在");

        SysUser after = SysUser.builder().id(param.getId()).username(param.getUsername()).telephone(param.getTelephone()).mail(param.getMail())
                .deptId(param.getDeptId()).status(param.getStatus()).remark(param.getRemark()).build();
        after.setOperator("system");
        after.setOperateTime(new Date());
        sysUserMapper.updateByPrimaryKeySelective(after);
    }

    public boolean checkEmailExists(String mail, Integer userId) {
        return sysUserMapper.countByMail(mail, userId) > 0;
    }

    public boolean checkTelephoneExists(String telephone, Integer userId) {
        return sysUserMapper.countByTelephone(telephone, userId) > 0;
    }

    public SysUser findByKeyword(String keyword) {
        return sysUserMapper.findByKeyword(keyword);
    }

    public PageResult<SysUser> getPageByDeptId(int deptId, PageQuery page) {
        BeanValidator.check(page);
        int count = sysUserMapper.countByDeptId(deptId);
        if (count > 0) {
            List<SysUser> list = sysUserMapper.getPageByDeptId(deptId, page);
            return PageResult.<SysUser>builder().total(count).data(list).build();
        }
        return PageResult.<SysUser>builder().build();
    }

    public List<SysUser> getAll() {
        return sysUserMapper.getAll();
    }
}
