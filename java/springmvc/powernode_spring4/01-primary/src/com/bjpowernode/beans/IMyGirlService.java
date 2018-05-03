package com.bjpowernode.beans;

import com.bjpowernode.service.Student;

import java.util.List;

/**
 * Created by bwhite on 18-4-30.
 */
public interface IMyGirlService {

    void addGirl(Girl girl);

    void removeGirl(int id);

    void modifyGirl(Girl girl);

    String findGirlNameById(int id);

    List<String> findGirlNames();

    Girl findGirlById(int id);

    List<Girl> findGirls();


}
