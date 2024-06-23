from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, stddev
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Analyzing Housing Data with PySpark") \
    .getOrCreate()

# Load generated housing data into PySpark DataFrame
df = spark.read.csv('generated_housing_data.csv', header=True, inferSchema=True)

# Show the first few rows and schema
df.show(5)
df.printSchema()

# Summary statistics
df.describe().show()

# Calculate average median house value and standard deviation of median income
avg_median_house_value = df.agg(avg('median_house_value')).collect()[0][0]
stddev_median_income = df.agg(stddev('median_income')).collect()[0][0]

print(f"Average Median House Value: {avg_median_house_value}")
print(f"Standard Deviation of Median Income: {stddev_median_income}")

# Visualization using Matplotlib (Example: Scatter plot of latitude vs. longitude)
plt.figure(figsize=(10, 6))
plt.scatter(df.toPandas()['longitude'], df.toPandas()['latitude'], c=df.toPandas()['median_house_value'], cmap='coolwarm', alpha=0.5)
plt.colorbar(label='Median House Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Geographical Distribution of Median House Value')
plt.show()

# Stop Spark session
spark.stop()
