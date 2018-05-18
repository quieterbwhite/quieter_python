CREATE TABLE keep.sys_role_acl
(
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    role_id INT NOT NULL COMMENT '角色id',
    acl_id INT NOT NULL COMMENT '权限id',
    operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
    operate_time DATETIME NOT NULL COMMENT '操作时间',
    operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '更新者ip'
);
ALTER TABLE keep.sys_role_acl COMMENT = '角色权限关系表';
