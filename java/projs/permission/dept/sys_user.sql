CREATE TABLE keep.sys_user
(
    id INT PRIMARY KEY NOT NULL COMMENT '用户id' AUTO_INCREMENT,
    username VARCHAR(20) DEFAULT '' NOT NULL COMMENT '用户名称',
    telephone VARCHAR(13) DEFAULT '' NOT NULL COMMENT '手机号',
    mail VARCHAR(20) DEFAULT '' NOT NULL COMMENT '邮箱',
    password VARCHAR(40) DEFAULT '' NOT NULL COMMENT '密码',
    dept_id INT DEFAULT 0 NOT NULL COMMENT '用户所在部门id',
    status INT DEFAULT 1 NOT NULL COMMENT '状态 1-正常 0-冻结 2-删除',
    remark VARCHAR(200) DEFAULT '' NOT NULL COMMENT '备注',
    operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
    operate_time DATETIME NOT NULL COMMENT '操作时间',
    operate_id VARCHAR(20) DEFAULT '' NOT NULL COMMENT '更新者ip'
);
ALTER TABLE keep.user COMMENT = '用户表';
