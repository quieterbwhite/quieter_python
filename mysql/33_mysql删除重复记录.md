# MYSQL 删除重复的数据

用SQL语句,删除掉重复项只保留一条

在几千条记录里,存在着些相同的记录,如何能用SQL语句,删除掉重复的呢

请留意红色部分

#### 1、查找表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断

```sql
SELECT
    *
FROM
    people
WHERE
    peopleId IN (
        SELECT
            peopleId
        FROM
            people
        GROUP BY
            peopleId
        HAVING
            count(peopleId) > 1
    )
```

#### 2、删除表中多余的重复记录，重复记录是根据单个字段（peopleId）来判断，只留有rowid最小的记录

```sql
DELETE
FROM
    people
WHERE
    peopleName IN (
        SELECT
            peopleName
        FROM
            people
        GROUP BY
            peopleName
        HAVING
            count(peopleName) > 1
    )
AND peopleId NOT IN (
    SELECT
        min(peopleId)
    FROM
        people
    GROUP BY
        peopleName
    HAVING
        count(peopleName) > 1
)
```

##### 执行上面的语句会现在的mysql中会提示：

执行报错：1093 - You can't specify target table 'student' for update in FROM clause 原因是：更新数据时使用了查询，而查询的数据又做了更新的条件，mysql不支持这种方式。 怎么规避这个问题？ 再加一层封装，如下：

```sql
DELETE
FROM
    people
WHERE
    peopleName IN (
         SELECT
            peopleName
        FROM(
             SELECT
                peopleName
            FROM
                people
            GROUP BY
                peopleName
            HAVING
                count(peopleName) > 1
        ) a
    )
AND peopleId NOT IN (
    SELECT
            peopleName
    FROM(
        SELECT
            min(peopleId)
        FROM
            people
        GROUP BY
            peopleName
        HAVING
            count(peopleName) > 1
    ) b
)
```

#### 3、查找表中多余的重复记录（多个字段）

```sql
SELECT
    *
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
```

#### 4、删除表中多余的重复记录（多个字段），只留有rowid最小的记录

```sql
DELETE
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
AND rowid NOT IN (
    SELECT
        min(rowid)
    FROM
        vitae
    GROUP BY
        peopleId,
        seq
    HAVING
        count(*) > 1
)
```

#### 5、查找表中多余的重复记录（多个字段），不包含rowid最小的记录

```sql
SELECT
    *
FROM
    vitae a
WHERE
    (a.peopleId, a.seq) IN (
        SELECT
            peopleId,
            seq
        FROM
            vitae
        GROUP BY
            peopleId,
            seq
        HAVING
            count(*) > 1
    )
AND rowid NOT IN (
    SELECT
        min(rowid)
    FROM
        vitae
    GROUP BY
        peopleId,
        seq
    HAVING
        count(*) > 1
)
```

#### 6.消除一个字段的左边的第一位：

```sql
UPDATE tableName 
    SET [ Title ]= RIGHT ([ Title ],(len([ Title ]) - 1))
WHERE
    Title LIKE '村%'
```

#### 7. 消除一个字段的右边的第一位：

```sql
UPDATE tableName
SET [ Title ]= LEFT ([ Title ],(len([ Title ]) - 1))
WHERE
    Title LIKE '%村'
```

#### 8.假删除表中多余的重复记录（多个字段），不包含rowid最小的记录

```sql
UPDATE tableName 
SET key = value WHERE key1 IN (
SELECT key1 FROM vitae GROUP BY peopleId)
```