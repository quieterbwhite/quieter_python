CREATE TABLE keep.sys_acl_module
(
    id INT PRIMARY KEY NOT NULL COMMENT '权限模块id' AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL COMMENT '权限模块名称',
    parent_id INT DEFAULT 0 NOT NULL COMMENT '上级权限模块id',
    level VARCHAR(200) DEFAULT '' NOT NULL COMMENT '权限模块层级',
    seq INT DEFAULT 0 NOT NULL COMMENT '权限模块在当前层级下的顺序,由小到大',
    status INT DEFAULT 1 NOT NULL COMMENT '状态 1-正常 0-冻结 2-删除',
    remark VARCHAR(200) DEFAULT '' COMMENT '备注',
    operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
    operate_time DATETIME DEFAULT now() NOT NULL COMMENT '操作时间',
    operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '最后操作者的ip'
);
ALTER TABLE keep.sys_dept COMMENT = '权限模块表';
