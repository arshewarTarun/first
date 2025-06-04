from pyspark.sql import SparkSession
import sys

try:
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("S3 to S3 Data Move") \
        .getOrCreate()

    # S3 paths
    input_path = "s3a://cdpmodakbucket/ta22_test/COLUMN.csv"
    #output_path = "s3a://j-and-j-test-bucket/target_combined_new_up"

    # Read Parquet file
    print(f"Reading from: {input_path}")
    df = spark.read.csv(input_path)



except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(1)

finally:
    # Stop the Spark session
    spark.stop()
    print("Spark session stopped.")
