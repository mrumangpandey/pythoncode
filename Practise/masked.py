
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit, regexp_extract, regexp_replace

# Create a Spark session
spark = SparkSession.builder.appName("MaskingData").getOrCreate()

# Input Data
data = [
 (1, "john.doe@gmail.com", "8956756457"),
 (2, "jane.smith@outlook.com", "9845671234"),
 (3, "alan.turing@yahoo.com", "9123456789"),
]
columns = ["id", "email", "phone"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Mask email
df = df.withColumn(
 "masked_email",
 concat(
 col("email").substr(1, 1), # First character of email
 lit("****"), # Masking part
 regexp_extract(col("email"), "@.*", 0) # Domain part starting from '@'
 )
)

# Mask phone
df = df.withColumn(
 "masked_phone",
 concat(
 lit("******"), # Masking part
 col("phone").substr(-4, 4) # Last 4 digits of phone number
 )
)

# Show the results
df.select("id", "masked_email", "masked_phone").show()