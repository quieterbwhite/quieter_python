package com.j2se.lesson6;

/**
 * Created by bwhite on 2017/10/6.
 */
public class Environment {

    private Strategy strategy;

    public Environment(Strategy strategy) {
        this.strategy = strategy;
    }

    public void setStrategy(Strategy strategy) {
        this.strategy = strategy;
    }

    public Strategy getStrategy() {
        return this.strategy;
    }

    public int calculate(int a, int b) {
        return this.strategy.calculata(a, b);
    }
}
