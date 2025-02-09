from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbtno_v2pythontrue00.config.ConfigStore import *
from automationpbtno_v2pythontrue00.functions import *

def reformatted_customer_data(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        concat(col("first_name"), col("last_name"), lit(Config.c_string), lit(Config.c_int), lit(Config.c_boolean))\
          .alias("col1"), 
        col("customer_id"), 
        col("first_name"), 
        col("last_name"), 
        col("phone"), 
        col("email"), 
        col("country_code"), 
        col("account_open_date"), 
        col("account_flags")
    )
