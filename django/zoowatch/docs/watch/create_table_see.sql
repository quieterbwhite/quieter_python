-- 监控
create table `watch` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `uid` INT NOT NULL DEFAULT 0,
    `openid` VARCHAR(50) NOT NULL COMMENT 'wechat openid',
    `shopid` INT NOT NULL COMMENT '店铺id',
    `content` TEXT COMMENT '内容',
    `is_pub` INT NOT NULL DEFAULT 0 COMMENT '0未发布1已发布',
    `created` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '创建时间',
    `updated` VARCHAR(32) NOT NULL DEFAULT '' COMMENT '最后更新时间',
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4';