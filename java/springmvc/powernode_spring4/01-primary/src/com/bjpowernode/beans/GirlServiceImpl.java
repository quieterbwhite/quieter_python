package com.bjpowernode.beans;

import com.bjpowernode.service.Student;

import java.util.List;

/**
 * Created by bwhite on 18-4-30.
 */
public class GirlServiceImpl implements IMyGirlService {

    private IGirlDao dao;

    public void setDao(IGirlDao dao) {
        this.dao = dao;
    }

    @Override
    public void addGirl(Girl girl) {
        dao.insertGirl(girl);
    }

    @Override
    public void removeGirl(int id) {
        dao.removeGirl(id);
    }

    @Override
    public void modifyGirl(Girl girl) {
        dao.modifyGirl(girl);
    }

    @Override
    public String findGirlNameById(int id) {
        return dao.findGirlNameById(id);
    }

    @Override
    public List<String> findGirlNames() {
        return dao.findGirlNames();
    }

    @Override
    public Girl findGirlById(int id) {
        return dao.findGirlById(id);
    }

    @Override
    public List<Girl> findGirls() {
        return dao.findGirls();
    }
}
