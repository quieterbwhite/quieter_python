package com.mmall.dao;

import com.mmall.model.SysDept;

public interface SysDeptMapper {
    int deleteByPrimaryKey(Integer id);

    // 全量插入所有字段
    int insert(SysDept record);

    // 只插入有值的字段
    int insertSelective(SysDept record);

    SysDept selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(SysDept record);

    int updateByPrimaryKey(SysDept record);
}