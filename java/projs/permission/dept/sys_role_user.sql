CREATE TABLE keep.sys_role_user
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  role_id INT NOT NULL COMMENT '角色id',
  user_id INT NOT NULL COMMENT '用户id',
  operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
  operate_time DATETIME NOT NULL COMMENT '操作时间',
  operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '更新者ip'
);
ALTER TABLE keep.sys_role_user COMMENT = '角色用户关系表';
