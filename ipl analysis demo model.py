# Databricks notebook source
# MAGIC %md
# MAGIC 1. DATA INGESTION ( BRONZE LAYER)

# COMMAND ----------

df = spark.read.table("workspace.default.match")
df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 2. CLEANING (SILVER LAYER) {Cleaned + structured data}
# MAGIC

# COMMAND ----------

from pyspark.sql.functions import col

# Remove rows where important columns are null
df_clean = df.dropna(subset=["Team1", "Team2"])

# Fill missing city with "Unknown"
df_clean = df_clean.fillna({"City_Name": "Unknown"})

# Remove duplicates (important in real data)
df_clean = df_clean.dropDuplicates()

df_clean.display()

# COMMAND ----------

# MAGIC %md
# MAGIC saving silver table
# MAGIC

# COMMAND ----------

df_clean.write.mode("overwrite").saveAsTable("workspace.default.ipl_silver_match")

# COMMAND ----------

# MAGIC %md
# MAGIC 3. feature engineering

# COMMAND ----------

# MAGIC %md
# MAGIC creating new column

# COMMAND ----------

from pyspark.sql.functions import year

df_feat = df_clean.withColumn("Year", year(col("match_date")))

# COMMAND ----------

# MAGIC %md
# MAGIC toss impact feature

# COMMAND ----------

df_feat = df_feat.withColumn(
    "Toss_Impact",
    col("Toss_Winner") == col("Match_Winner")
)

df_feat.display()

# COMMAND ----------

# MAGIC %md
# MAGIC 4. DATA ANALYSIS (gold insights) & VISUALIZATION
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC team wins

# COMMAND ----------

team_wins = df_feat.groupBy("Match_Winner").count() \
    .orderBy("count", ascending=False)

display(team_wins)

# COMMAND ----------

# MAGIC %md
# MAGIC matches per person

# COMMAND ----------

matches_per_season = df_feat.groupBy("Season_Year").count()

display(matches_per_season)

# COMMAND ----------

# MAGIC %md
# MAGIC toss impact analysis

# COMMAND ----------

toss_impact = df_feat.groupBy("Toss_Impact").count()

display(toss_impact)

# COMMAND ----------

# MAGIC %md
# MAGIC matches by city

# COMMAND ----------

city_matches = df_feat.groupBy("City_Name").count()

display(city_matches)

# COMMAND ----------

team_wins.write.mode("overwrite").saveAsTable("workspace.default.ipl_gold_team_wins")

# COMMAND ----------

display(team_wins.limit(10))