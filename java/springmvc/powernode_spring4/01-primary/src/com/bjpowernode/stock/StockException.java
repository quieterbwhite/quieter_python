package com.bjpowernode.stock;

/**
 * Created by bwhite on 18-5-3.
 */
public class StockException extends Exception {

    public StockException(){
        super();
    }

    public StockException(String message) {
        super(message);
    }
}
