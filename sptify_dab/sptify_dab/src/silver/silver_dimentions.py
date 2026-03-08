# Databricks notebook source
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

import os 
import sys

project_pth = os.path.join(os.getcwd(),'..','..')
sys.path.append(project_pth)

from utils.transformations import reusable

# COMMAND ----------

# MAGIC %md
# MAGIC ###DimUser

# COMMAND ----------

df = spark.read.format("parquet")\
    .load("abfss://bronze@lkazureproject.dfs.core.windows.net/DimUser")

# COMMAND ----------

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Auto Loader

# COMMAND ----------

df_user = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@lkazureproject.dfs.core.windows.net/schema/DimUser")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@lkazureproject.dfs.core.windows.net/DimUser")


# COMMAND ----------

display_checkpoint = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display"
display(df_user, checkpointLocation=display_checkpoint)

# COMMAND ----------

df_user = df_user.withColumn("user_name",upper(col("user_name")))

# COMMAND ----------

df_user_obj = reusable()

df_user = df_user_obj.dropColumns(df_user,['_rescued_data'])
df_user = df_user.dropDuplicates(['user_id'])
display_checkpoint1 = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display1"
display(df_user, checkpointLocation=display_checkpoint1)

# COMMAND ----------

df_user.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/DimUser")\
            .trigger(once=True)\
            .option("path","abfss://silver@lkazureproject.dfs.core.windows.net/tables/DimUser/data")\
            .toTable("spotify_catalog.silver.DimUser")

# COMMAND ----------

# MAGIC %md
# MAGIC ###DIMARTIST
# MAGIC

# COMMAND ----------

df_artist = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format", "parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@lkazureproject.dfs.core.windows.net/schema/DimUser/checkpoints/DimArtist")\
            .option("schemaEvolutionMode", "addNewColumns")\
            .load("abfss://bronze@lkazureproject.dfs.core.windows.net/DimArtist")

# COMMAND ----------

display(df_artist, checkpointLocation = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display2")

# COMMAND ----------

df_artist_obj = reusable()
df_artist = df_artist_obj.dropColumns(df_artist, ['_rescued_data'])
df_artist = df_artist_obj.dropColumns(df_artist,['artist_id'])
display(df_artist, checkpointLocation = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display5")

# COMMAND ----------

df_artist.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/DimArtist") \
    .trigger(once=True) \
    .option("path", "abfss://silver@lkazureproject.dfs.core.windows.net/tables/DimArtist")\
    .toTable("spotify_catalog.silver.DimArtist")

# COMMAND ----------

# MAGIC %md
# MAGIC ###DimTrack

# COMMAND ----------

df_track = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@lkazureproject.dfs.core.windows.net/schema/Dimtrack/checkpoints/DimTrack")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@lkazureproject.dfs.core.windows.net/DimTrack")

# COMMAND ----------

display(df_track, checkpointLocation = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display3")

# COMMAND ----------

df_track = df_track.withColumn("durationFlag",when(col('duration_sec')<150,"low")\
                                            .when(col('duration_sec')<300,"medium")\
                                            .otherwise("high"))

df_track = df_track.withColumn("track_name",regexp_replace(col('track_name'),'-',' '))

df_track = reusable().dropColumns(df_track,['_rescued_data'])
display(df_track, checkpointLocation = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display4")

# COMMAND ----------

df_track.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/DimTrack")\
            .trigger(once=True)\
            .option("path","abfss://silver@lkazureproject.dfs.core.windows.net/tables/DimTrack/data")\
            .toTable("spotify_catalog.silver.DimTrack")

# COMMAND ----------

# MAGIC %md
# MAGIC ###DimDate

# COMMAND ----------

df_date = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@lkazureproject.dfs.core.windows.net/schema/checkpoints/DimDate")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@lkazureproject.dfs.core.windows.net/DimDate")

# COMMAND ----------

df_date = reusable().dropColumns(df_date,['_rescued_data'])

df_date.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/DimDate")\
            .trigger(once=True)\
            .option("path","abfss://silver@lkazureproject.dfs.core.windows.net/tables/DimDate/data")\
            .toTable("spotify_catalog.silver.DimDate")

# COMMAND ----------

# MAGIC %md
# MAGIC ###FactStream

# COMMAND ----------

# DBTITLE 1,Load FactStream data
df_fact = spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format","parquet")\
            .option("cloudFiles.schemaLocation","abfss://silver@lkazureproject.dfs.core.windows.net/schema/checkpoints/FactStream")\
            .option("schemaEvolutionMode","addNewColumns")\
            .load("abfss://bronze@lkazureproject.dfs.core.windows.net/FactStream")

# COMMAND ----------

display(df_fact, checkpointLocation = "abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/display6")

# COMMAND ----------

df_fact = reusable().dropColumns(df_fact,['_rescued_data'])

df_fact.writeStream.format("delta")\
            .outputMode("append")\
            .option("checkpointLocation","abfss://silver@lkazureproject.dfs.core.windows.net/checkpoints/FactStream")\
            .trigger(once=True)\
            .option("path","abfss://silver@lkazureproject.dfs.core.windows.net/tables/FactStream/data")\
            .toTable("spotify_catalog.silver.FactStream")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM spotify_catalog.gold.dimtrack
# MAGIC WHERE  `__END_AT` IS NOT NULL

# COMMAND ----------

