package com.bjpowernode.stock;

/**
 * Created by bwhite on 18-5-1.
 */
public interface IAccountDao {

    void insertAccount(String aname, double money);

    void updateAccount(String aname, double money, boolean isBuy);
}
