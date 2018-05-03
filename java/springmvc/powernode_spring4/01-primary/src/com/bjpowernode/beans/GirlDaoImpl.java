package com.bjpowernode.beans;

import org.springframework.jdbc.core.support.JdbcDaoSupport;

import java.util.List;

/**
 * Created by bwhite on 18-4-30.
 */
public class GirlDaoImpl extends JdbcDaoSupport implements IGirlDao {

    @Override
    public void insertGirl(Girl girl) {
        System.out.println("insertGirl girl=" + girl);
        String sql = "insert into girl(age, cup_size) values(?, ?)";
        // 可变参数
        this.getJdbcTemplate().update(sql, girl.getAge(), girl.getcup_size());
    }

    @Override
    public void removeGirl(int id) {
        System.out.println("GirlDaoImpl - removeGirl - id:" + id);
        String sql = "delete from girl where id = ?";
        this.getJdbcTemplate().update(sql, id);
    }

    @Override
    public void modifyGirl(Girl girl) {
        String sql = "update girl set age=?, cup_size=? where id=?";
        this.getJdbcTemplate().update(sql, girl.getAge(), girl.getcup_size(), girl.getId());
    }

    @Override
    public String findGirlNameById(int id) {
        String sql = "select name from girl where id = ?";
        return this.getJdbcTemplate().queryForObject(sql, String.class, id);
    }

    @Override
    public List<String> findGirlNames() {
        String sql = "select name from girl";
        return this.getJdbcTemplate().queryForList(sql, String.class);
    }

    @Override
    public Girl findGirlById(int it) {
        return null;
    }

    @Override
    public List<Girl> findGirls() {
        return null;
    }
}
