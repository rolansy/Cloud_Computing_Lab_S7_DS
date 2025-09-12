from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read text file
text_file = spark.sparkContext.textFile("input.txt")

# Split lines into words
words = text_file.flatMap(lambda line: line.split(" "))

# Count each word
word_counts = words.map(lambda word: (word, 1)) \
                   .reduceByKey(lambda a, b: a + b)
print(word_counts)
# Collect results and print
for word, count in word_counts.collect():
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
