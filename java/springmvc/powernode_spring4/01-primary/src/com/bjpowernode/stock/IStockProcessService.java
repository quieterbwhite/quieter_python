package com.bjpowernode.stock;

/**
 * Created by bwhite on 18-5-1.
 */
public interface IStockProcessService {

    void openAccount(String aname, double money);

    void openStock(String sname, int amount);

    void buyStock(String aname, double money, String sname, int amount);

}
