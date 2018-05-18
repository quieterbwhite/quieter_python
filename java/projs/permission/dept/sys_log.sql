CREATE TABLE keep.sys_log
(
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  type INT DEFAULT 0 NOT NULL COMMENT '权限更新的类型,1:部门,2:用户，3:权限模块, 4:权限, 5:角色，6：角色用户关系, 7:角色权限关系',
  target_id INT NOT NULL COMMENT '基于type后指定的对象id,比如用户，权限，角色等表的主键',
  old_value TEXT COMMENT '旧值',
  new_value TEXT COMMENT '新值',
  operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
  operate_time DATETIME NOT NULL COMMENT '操作时间',
  operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '更新者ip',
  status INT DEFAULT 0 NOT NULL COMMENT '当前是否复原过,0:没有，1:复原过'
);
ALTER TABLE keep.sys_log COMMENT = '权限日志表';
