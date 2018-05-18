CREATE TABLE keep.sys_role
(
    id INT PRIMARY KEY NOT NULL COMMENT '用户id' AUTO_INCREMENT,
    name VARCHAR(20) DEFAULT '' NOT NULL COMMENT '名称',
    type INT DEFAULT 1 NOT NULL COMMENT '角色类型,1:管理员角色,2:其他',
    status INT DEFAULT 1 NOT NULL COMMENT '状态 1-正常 0-冻结',
    remark VARCHAR(200) DEFAULT '' NOT NULL COMMENT '备注',
    operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
    operate_time DATETIME NOT NULL COMMENT '操作时间',
    operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '更新者ip'
);
ALTER TABLE keep.user COMMENT = '角色表';
