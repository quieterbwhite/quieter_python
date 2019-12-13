-- 监控
create table `me` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `title` VARCHAR(50) NOT NULL COMMENT '标题',
    primary key (`id`)
) ENGINE=InnoDB DEFAULT CHARSET='utf8mb4';