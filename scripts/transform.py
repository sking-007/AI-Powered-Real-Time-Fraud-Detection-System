from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("FraudDetection").getOrCreate()

df = spark.read.csv("data/raw_transactions.csv", header=True, inferSchema=True)

# Data Cleaning & Feature Engineering
df_cleaned = df.dropna()
df_cleaned = df_cleaned.withColumn("amount", col("amount").cast("float"))

df_cleaned.write.csv("data/processed_transactions.csv", header=True)
print("Data transformed successfully!")
