## [spark计算两个DataFrame的差集、交集、合集](https://www.cnblogs.com/TTyb/p/7991952.html)

`spark` 计算两个`dataframe` 的差集、交集、合集，只选择某一列来对比比较好。新建两个 `dataframe` ：

```
import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.SQLContext

def main(args: Array[String]): Unit = {

    val conf = new SparkConf().setAppName("TTyb").setMaster("local")
    val sc = new SparkContext(conf)
    val spark = new SQLContext(sc)
    val sentenceDataFrame = spark.createDataFrame(Seq(
      (1, "asf"),
      (2, "2143"),
      (3, "rfds")
    )).toDF("label", "sentence")
    sentenceDataFrame.show()

    val sentenceDataFrame1 = spark.createDataFrame(Seq(
      (1, "asf"),
      (2, "2143"),
      (4, "f8934y")
    )).toDF("label", "sentence")
    sentenceDataFrame1.show()
}
```

### 差集 except

```
val newDF = sentenceDataFrame1.select("sentence").except(sentenceDataFrame.select("sentence"))
newDF.show()
```

+--------+
|sentence|
+--------+
|f8934y |
+--------+

### 交集 intersect

```
val newDF = sentenceDataFrame1.select("sentence").intersect(sentenceDataFrame.select("sentence"))
newDF.show()
```

+--------+
|sentence|
+--------+
| asf|
| 2143|
+--------+

### 合集 union

```
val newDF = sentenceDataFrame1.select("sentence").union(sentenceDataFrame.select("sentence"))
newDF.show()
```

+--------+
|sentence|
+--------+
| asf|
| 2143|
| f8934y|
| asf|
| 2143|
| rfds|
+--------+

合集最好去一下重 `distinct` ：

```
val newDF = sentenceDataFrame1.select("sentence").union(sentenceDataFrame.select("sentence")).distinct()
newDF.show()
```

+--------+
|sentence|
+--------+
| rfds|
| asf|
| 2143|
| f8934y|
+--------+