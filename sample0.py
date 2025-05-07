from pyspark.sql import SparkSession
import sys

try:
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("S3 to S3 Data Move") \
        .getOrCreate()

    # S3 paths
    input_path = "s3a://j-and-j-test-bucket/target_combined_new/part-00000-ce9be0cc-25d3-470b-9745-19c501275b30-c000.snappy.parquet"
    output_path = "s3a://j-and-j-test-bucket/target_combined_new_up"

    # Read Parquet file
    print(f"Reading from: {input_path}")
    df = spark.read.parquet(input_path)

    # Show the DataFrame
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    df.show()
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    # Write to output path
    print(f"Writing to: {output_path}")
    df.write.mode("overwrite").parquet(output_path)
    print("Write operation completed successfully.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
    sys.exit(1)

finally:
    # Stop the Spark session
    spark.stop()
    print("Spark session stopped.")
