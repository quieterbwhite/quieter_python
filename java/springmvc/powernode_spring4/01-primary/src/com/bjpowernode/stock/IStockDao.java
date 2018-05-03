package com.bjpowernode.stock;

/**
 * Created by bwhite on 18-5-1.
 */
public interface IStockDao {

    void insertStock(String sname, int amount);

    void updateStock(String sname, int amount, boolean isBuy);
}
