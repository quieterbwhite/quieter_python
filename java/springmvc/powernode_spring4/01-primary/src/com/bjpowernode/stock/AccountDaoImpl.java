package com.bjpowernode.stock;

import org.springframework.jdbc.core.support.JdbcDaoSupport;

/**
 * Created by bwhite on 18-5-1.
 */
public class AccountDaoImpl extends JdbcDaoSupport implements IAccountDao {

    @Override
    public void insertAccount(String aname, double money) {
        String sql = "insert into account(aname, balance) values(?, ?)";
        this.getJdbcTemplate().update(sql, aname, money);
    }

    @Override
    public void updateAccount(String aname, double money, boolean isBuy) {
        String sql = "update account set balance=balance+? where aname=?";
        if(isBuy) {
            sql = "update account set balance=balance-? where aname=?";
        }
        this.getJdbcTemplate().update(sql, money, aname);
    }
}
