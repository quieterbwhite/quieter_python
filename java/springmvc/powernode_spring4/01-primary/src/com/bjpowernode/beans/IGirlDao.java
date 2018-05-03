package com.bjpowernode.beans;

import java.util.List;

/**
 * Created by bwhite on 18-4-30.
 */
public interface IGirlDao {

    void insertGirl(Girl girl);

    void removeGirl(int id);

    void modifyGirl(Girl girl);

    String findGirlNameById(int id);

    List<String> findGirlNames();

    Girl findGirlById(int it);

    List<Girl> findGirls();
}
