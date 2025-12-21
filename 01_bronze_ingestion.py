import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.getOrCreate()

url = "https://api.coinbase.com/v2/assets/prices?base=BRL"
response = requests.get(url).json()

data = response["data"]

df = spark.createDataFrame(data)

df_bronze = df.withColumn(
    "ingestion_timestamp",
    current_timestamp()
)

df_bronze.write.format("delta") \
    .mode("append") \
    .saveAsTable("default.bronze_crypto_prices")

