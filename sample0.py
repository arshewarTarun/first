from pyspark.sql import SparkSession
import sys

try:
    spark = SparkSession.builder \
        .appName("S3 to S3 Data Move") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .getOrCreate()

    input_path = "s3a://cdpmodakbucket/ta22_test/COLUMN.csv"

    print(f"Reading from: {input_path}")
    df = spark.read.option("header", "true").csv(input_path)
    df.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(1)

finally:
    spark.stop()
    print("Spark session stopped.")
