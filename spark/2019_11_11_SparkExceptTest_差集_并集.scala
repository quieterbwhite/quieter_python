package com.ufm.dp.test

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.sql.{Row, SQLContext}

/*
spark 计算两个dataframe 的差集、交集、合集，只选择某一列来对比比较好。新建两个 dataframe ：
https://www.cnblogs.com/TTyb/p/7991952.html
 */

object SparkExceptTest {

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

    // 差集 except
    val exceptDF = sentenceDataFrame.select("sentence").except(sentenceDataFrame1.select("sentence"))
    exceptDF.show()

    // 交集 intersect
    val intersectDF = sentenceDataFrame1.select("sentence").intersect(sentenceDataFrame.select("sentence"))
    intersectDF.show()

    // 合集 union
    val unionDF = sentenceDataFrame1.select("sentence").union(sentenceDataFrame.select("sentence"))
    unionDF.show()

    // 合集最好去一下重 distinct：
    val distinctDF = sentenceDataFrame1.select("sentence").union(sentenceDataFrame.select("sentence")).distinct()
    distinctDF.show()

  }

}
