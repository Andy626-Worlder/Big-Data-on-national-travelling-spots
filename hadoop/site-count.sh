#!/bin/bash

# 计算出现次数


# create input directory on HDFS
hadoop fs -mkdir -p input

# put input files to HDFS
hdfs dfs -put ./input/* input

# run wordcount
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/sources/hadoop-mapreduce-examples-2.7.2-sources.jar org.apache.hadoop.examples.WordCount input output


# print the output of wordcount
echo -e "\nwordcount output:"
hdfs dfs -cat output/part-r-00000