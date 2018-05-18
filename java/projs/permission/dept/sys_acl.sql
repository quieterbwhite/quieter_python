CREATE TABLE keep.sys_acl
(
    id INT PRIMARY KEY NOT NULL COMMENT '权限id' AUTO_INCREMENT,
    code VARCHAR(20) NOT NULL COMMENT '权限码',
    name VARCHAR(20) NOT NULL COMMENT '权限名称',
    acl_module_id INT DEFAULT 0 NOT NULL COMMENT '权限所在的权限模块id',
    url VARCHAR(100) DEFAULT '' NOT NULL COMMENT '请求的url,可以填正则表达式',
    type INT DEFAULT 3 NOT NULL COMMENT '类型,1:菜单,2:按钮,3:其他',
    status INT DEFAULT 1 NOT NULL COMMENT '状态,1:正常,0:冻结',
    seq INT DEFAULT 0 NOT NULL COMMENT '权限在当前模块下的顺序，由小到大',
    remark VARCHAR(200) DEFAULT '' NOT NULL COMMENT '备注',
    operator VARCHAR(20) DEFAULT '' NOT NULL COMMENT '操作者',
    operate_time DATETIME DEFAULT now() NOT NULL COMMENT '操作时间',
    operate_ip VARCHAR(20) DEFAULT '' NOT NULL COMMENT '最后操作者的ip'
);
ALTER TABLE keep.sys_acl COMMENT = '权限表';
