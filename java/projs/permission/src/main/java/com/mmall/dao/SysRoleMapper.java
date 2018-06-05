package com.mmall.dao;

import com.mmall.model.SysRole;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface SysRoleMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(SysRole record);

    int insertSelective(SysRole record);

    SysRole selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(SysRole record);

    int updateByPrimaryKey(SysRole record);

    List<SysRole> getAll();

    int countByName(@Param("name") String name, @Param("id") Integer id);

    List<SysRole> getByIdList(@Param("idList") List<Integer> idList);
}