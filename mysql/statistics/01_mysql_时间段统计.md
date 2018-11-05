#### Mysql 时间操作（当天，昨天，7天，30天，半年，全年，季度）

> https://blog.csdn.net/u012087785/article/details/50402391

2015年12月25日 12:17:59 [_devin](https://me.csdn.net/u012087785) 阅读数：10227



1 、 查看当天日期

select current_date();

 

2、 查看当天时间

select current_time();

 

3、查看当天时间日期

select current_timestamp();

 

4、查询当天记录

select * from 表名 where to_days(时间字段名) = to_days(now());

 

5、查询昨天记录

SELECT * FROM 表名 WHERE TO_DAYS( NOW( ) ) – TO_DAYS( 时间字段名) <= 1

 

6、查询7天的记录

SELECT * FROM 表名 where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(时间字段名) 

 

7、查询近30天的记录

SELECT * FROM 表名 where DATE_SUB(CURDATE(), INTERVAL 30 DAY) <= date(时间字段名)

 

8、查询本月的记录

SELECT * FROM 表名 WHERE DATE_FORMAT( 时间字段名, ‘%Y%m’ ) = DATE_FORMAT( CURDATE( ) , ‘%Y%m’ )

 

9、查询上一月的记录

SELECT * FROM 表名 WHERE PERIOD_DIFF( date_format( now( ) , ‘%Y%m’ ) , date_format( 时间字段名, ‘%Y%m’ ) ) =1

 

10、查询本季度数据

select * from 表名 where QUARTER(create_date)=QUARTER(now());



11、查询上季度数据
select * from 表名 where QUARTER(create_date)=QUARTER(DATE_SUB(now(),interval 1 QUARTER));

 

12、查询本年数据
select * from 表名  where YEAR(create_date)=YEAR(NOW());

 

13、查询上年数据
select * from 表名 where year(create_date)=year(date_sub(now(),interval 1 year));



14、查询当前这周的数据 
SELECT * FROM 表名 WHERE YEARWEEK(date_format(submittime,'%Y-%m-%d')) = YEARWEEK(now());

 

15、查询上周的数据
SELECT * FROM 表名 WHERE YEARWEEK(date_format(submittime,'%Y-%m-%d')) = YEARWEEK(now())-1;

 

16、查询当前月份的数据
select * from 表名   where date_format(submittime,'%Y-%m')=date_format(now(),'%Y-%m')

 

17、查询距离当前现在6个月的数据
select name,submittime from enterprise where submittime between date_sub(now(),interval 6 month) and now();

---

limit_rule_record ： 表名
create_time ：创建时间

一、按自然年
SELECT * FROM limit_rule_record WHERE create_time >= CURRENT_TIMESTAMP - INTERVAL 1 year

二、按自然月
SELECT * FROM limit_rule_record WHERE create_time >= CURRENT_TIMESTAMP - INTERVAL 1 MONTH

三、按自然日
SELECT * FROM limit_rule_record WHERE create_time >= CURRENT_TIMESTAMP - INTERVAL 1 DAY

四、按季度
SELECT * FROM limit_rule_record WHERE create_time >= CURRENT_TIMESTAMP - INTERVAL 1 quarter

五、按周

SELECT * FROM limit_rule_record WHERE create_time >= CURRENT_TIMESTAMP - INTERVAL 7 DAY

---

##### MySql按周，按月，按日分组统计数据

> https://blog.csdn.net/lqclh502/article/details/50157483

2015年12月03日 10:38:30

知识关键词：DATE_FORMAT

```
    select DATE_FORMAT(create_time,'%Y%u') weeks,count(caseid) count from tc_case group by weeks;  
    select DATE_FORMAT(create_time,'%Y%m%d') days,count(caseid) count from tc_case group by days;  
    select DATE_FORMAT(create_time,'%Y%m') months,count(caseid) count from tc_case group by months; 123
```

**如果是需要补全缺少的月份, 有两种方式:**

​    **1. 和一张完整的时间表左连接**  https://bbs.csdn.net/topics/360237845

​    **2. 数据查询出来在代码里面检查处理**

DATE_FORMAT(date,format)

根据format字符串格式化date值。下列修饰符可以被用在format字符串中：

%M 月名字(January……December) 
%W 星期名字(Sunday……Saturday) 
%D 有英语前缀的月份的日期(1st, 2nd, 3rd, 等等。） 
%Y 年, 数字, 4 位 
%y 年, 数字, 2 位 
%a 缩写的星期名字(Sun……Sat) 
%d 月份中的天数, 数字(00……31) 
%e 月份中的天数, 数字(0……31) 
%m 月, 数字(01……12) 
%c 月, 数字(1……12) 
%b 缩写的月份名字(Jan……Dec) 
%j 一年中的天数(001……366) 
%H 小时(00……23) 
%k 小时(0……23) 
%h 小时(01……12) 
%I 小时(01……12) 
%l 小时(1……12) 
%i 分钟, 数字(00……59) 
%r 时间,12 小时(hh:mm:ss [AP]M) 
%T 时间,24 小时(hh:mm:ss) 
%S 秒(00……59) 
%s 秒(00……59) 
%p AM或PM 
%w 一个星期中的天数(0=Sunday ……6=Saturday ） 
%U 星期(0……52), 这里星期天是星期的第一天 
%u 星期(0……52), 这里星期一是星期的第一天 
%% 一个文字“%”。

应用实例： 
1.按月统计各功能用量

```mysql
SELECT 
  DATE_FORMAT(`date`, '%Y%m') months,
  SUM(itemstatnum) sumnum 
FROM
  statnum 
WHERE `date` > '2015-01-01 00:00:00' 
  AND statitemid = 25 
GROUP BY months ;12345678
```

2.按省份分月统计功能用量

```mysql
SELECT 
  DATE_FORMAT(sn.`date`, '%Y%m') months,
  qae.`province_name`,
  SUM(sn.itemstatnum) sumnum,
  qae.`belong_to_province` prov 
FROM
  statnum sn,
  qw_authorized_ecbind qae 
WHERE sn.`entid` = qae.`grp_id` 
  AND `date` > '2015-09-01 00:00:00' 
  AND statitemid = 100 
GROUP BY months,
  prov ;
```


##### 我自己写的

```mysql
@Select("select IFNULL(DATE_FORMAT(create_time,'%c'), '') months, IFNULL(sum(bad_balance), 0) badBalanceCountMonth, IFNULL(sum(debit_interest), 0) debitInterestCountMonth, IFNULL(sum(recovered_amount), 0) recycleCountMonth from v_case_proxy where bank_user_id = #{bank_user_id} and is_deleted=1 and create_time between date_sub(now(),interval #{month_range} month) and now() group by months")

@Select("select IFNULL(DATE_FORMAT(create_time, '%c'), '') months, IFNULL(sum(bad_balance), 0) badBalanceCountMonth, IFNULL(sum(debit_interest), 0) debitInterestCountMonth, IFNULL(sum(recovered_amount), 0) recycleCountMonth from v_case_proxy where bank_id = #{bank_id} and is_deleted=1 and YEAR(create_time) = #{year} group by months")
```

```java
/**
 * 获取完整月份跨度数据列表
 * @param caseMonthRange
 * @return
 */
private ArrayList<String> getMonthRange(Integer caseMonthRange) {
    ArrayList<String> dateArray = new ArrayList<>();
    Date now = new Date();
    Calendar cal = Calendar.getInstance();
    cal.setTime(now);
    for (int i = 0; i < caseMonthRange; i++) {
        dateArray.add(DateUtil.formateMonth(cal.getTime()));
        cal.add(Calendar.MONTH, -1);
    }
    Collections.reverse(dateArray);
    return dateArray;
}

/**
 * 统计相关常量
 */
public interface StatisticsConstants {

    /**
     * 月份
     */
    ArrayList<String> monthArrayList = new ArrayList<>(
            Arrays.asList("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"));
}

/**
 * 年份, 默认值: 当前年份
 */
@ApiModelProperty(value = "年份")
private String year = String.valueOf(Calendar.getInstance().get(Calendar.YEAR));
```

