//adding new line july 11_0
//adding new line july 11_1
//adding new line july 11
//adding new line july-10

import org.apache.spark.sql.{SparkSession, DataFrame}

import org.apache.spark.sql.types.StructType
 
object PostgresParquetComparator {
 
  def main(args: Array[String]): Unit = {
 
    val spark = SparkSession.builder()

      .appName("Compare Postgres and Parquet")

      .master("local[*]") // remove or change this for cluster mode

      .getOrCreate()
   //s3 connection config
   
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.access.key", "ACCESS_KEY")
   
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.secret.key", "SECRET_KEY")
   
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.endpoint", "s3.amazonaws.com")
   
    spark.sparkContext.hadoopConfiguration.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
 
    // PostgreSQL connection config

    val pgUrl = "URL"

    val pgTable = "TABLE"

    val pgUser = "USER"

    val pgPassword = "PASSWORD"
 
    // Path to the Parquet file

    val parquetPath = "PATH"
 
    // Read PostgreSQL table

    val pgDF: DataFrame = spark.read

      .format("jdbc")

      .option("url", pgUrl)

      .option("dbtable", pgTable)

      .option("user", pgUser)

      .option("password", pgPassword)

      .option("driver", "org.postgresql.Driver")

      .load()
 
    // Read Parquet file

    val parquetDF: DataFrame = spark.read.parquet(parquetPath)
 
    // Compare row counts

    val pgCount = pgDF.count()

    val parquetCount = parquetDF.count()
 
    println(s"PostgreSQL row count: $pgCount")

    println(s"Parquet row count   : $parquetCount")
 
    // Compare schemas

    val pgSchema: StructType = pgDF.schema

    val parquetSchema: StructType = parquetDF.schema
 
    val schemaEqual = pgSchema.equals(parquetSchema)

    println(s"Schemas are equal: $schemaEqual")
 
    if (!schemaEqual) {

      println("PostgreSQL Schema:")

      pgSchema.printTreeString()
 
      println("Parquet Schema:")

      parquetSchema.printTreeString()

    }
 
    spark.stop()

  }

}

 
