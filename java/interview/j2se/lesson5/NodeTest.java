package com.j2se.lesson5;

/**
 * Created by bwhite on 17-10-4.
 */
public class NodeTest {

    public static void main(String[] args) {

        Node node1 = new Node("node1");
        Node node2 = new Node("node2");
        Node node3 = new Node("node3");

        node1.next = node2;
        node2.next = node3;

        System.out.println(node1.next.next.data);

    }

}
