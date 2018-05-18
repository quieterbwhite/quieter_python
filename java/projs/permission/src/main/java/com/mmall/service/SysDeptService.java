package com.mmall.service;

import com.mmall.dao.SysDeptMapper;
import com.mmall.exception.ParamException;
import com.mmall.model.SysDept;
import com.mmall.param.DeptParam;
import com.mmall.util.BeanValidator;
import com.mmall.util.LevelUtil;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.Date;

/**
 * Created by bwhite on 18-5-18.
 */
@Service
public class SysDeptService {

    @Resource
    private SysDeptMapper sysDeptMapper;

    public void save(DeptParam deptParam) {

        BeanValidator.check(deptParam);

        if (checkExists(deptParam.getParentId(), deptParam.getName(), deptParam.getId())) {
            throw new ParamException("同一层级下存在相同名称的部门");
        }

        // 使用 lombok 的 build 功能就能生成类
        SysDept debt = SysDept.builder()
                            .name(deptParam.getName())
                            .parentId(deptParam.getParentId())
                            .seq(deptParam.getSeq())
                            .remark(deptParam.getRemark())
                            .build();

        debt.setLevel(LevelUtil.calculateLevel(getLevel(deptParam.getParentId()), deptParam.getParentId()));
        debt.setOperator("system");
        debt.setOperateTime(new Date());
        debt.setOperateIp("127.0.0.1");
        sysDeptMapper.insert(debt);
    }

    private boolean checkExists(Integer parentId, String deptName, Integer deptId) {

        // TODO
        return true;
    }

    private String getLevel(Integer deptId) {
        SysDept dept = sysDeptMapper.selectByPrimaryKey(deptId);
        if (dept == null) {
            return null;
        }

        return dept.getLevel();
    }
}
