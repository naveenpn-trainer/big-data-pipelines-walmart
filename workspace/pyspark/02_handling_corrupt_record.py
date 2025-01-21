from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
if __name__ == '__main__':
    spark = SparkSession.builder.appName("Spark Streaming Demo").master("local").getOrCreate()
    user_df = spark.read.json("../../resources/dataset/access_logs.json",
                              mode="FAILFAST")
    user_df.show()