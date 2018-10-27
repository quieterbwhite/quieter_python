#### Mysql 视图



##### 用过的命令

```mysql
# 创建或者更新视图
create or replace view V_case_proxy AS select `a`.`case_id` AS `case_id`,`a`.`case_stage` AS `case_stage`,`a`.`bank_id` AS `bank_id`,`a`.`customer_no` AS `customer_no`,`a`.`customer_name` AS `customer_name`,`a`.`customer_type` AS `customer_type`,`a`.`bad_balance` AS `bad_balance`,`a`.`debit_interest` AS `debit_interest`,`a`.`last_urge_time` AS `last_urge_time`,`a`.`lawsuit_expiry_time` AS `lawsuit_expiry_time`,`a`.`dict_lawsuit_stage` AS `dict_lawsuit_stage`,`a`.`case_status` AS `case_status`,`a`.`last_remind_time` AS `last_remind_time`,`a`.`is_deleted` AS `is_deleted`,`a`.`create_time` AS `create_time`,`b`.`proxy_id` AS `proxy_id`,`b`.`group_id` AS `group_id`,`b`.`bank_user_id` AS `bank_user_id`,`b`.`firm_id` AS `firm_id`,`b`.`firm_user_id` AS `firm_user_id`,`b`.`proxy_type` AS `proxy_type`,`b`.`proxy_start_date` AS `proxy_start_date`,`b`.`proxy_end_date` AS `proxy_end_date`,`b`.`rate` AS `rate`,`b`.`recovered_amount` AS `recovered_amount`,`b`.`create_time` AS `split_case_time` from (`zas_case` `a` join `zas_case_proxy` `b`) where ((`a`.`case_id` = `b`.`case_id`) and (`b`.`is_deleted` = 1));

```

