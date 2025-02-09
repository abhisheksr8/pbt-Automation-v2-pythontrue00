from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbtno_v2pythontrue00.config.ConfigStore import *
from automationpbtno_v2pythontrue00.functions import *

def s3_source_dataset(spark: SparkSession) -> DataFrame:
    return spark.read.format("parquet").load("s3a://qa-prophecy/datasets/parquet/customers")
