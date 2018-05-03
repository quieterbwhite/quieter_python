package com.bjpowernode.stock;

/**
 * Created by bwhite on 18-5-1.
 */
public class Account {

    private Integer aid;

    private String aname;

    private Double balance;

    public Account() {
    }

    public Account(String aname, Double balance) {
        this.aname = aname;
        this.balance = balance;
    }

    public Integer getAid() {
        return aid;
    }

    public void setAid(Integer aid) {
        this.aid = aid;
    }

    public String getAname() {
        return aname;
    }

    public void setAname(String aname) {
        this.aname = aname;
    }

    public Double getBalance() {
        return balance;
    }

    public void setBalance(Double balance) {
        this.balance = balance;
    }

    @Override
    public String toString() {
        return "Account{" +
                "aid=" + aid +
                ", aname='" + aname + '\'' +
                ", balance=" + balance +
                '}';
    }
}
