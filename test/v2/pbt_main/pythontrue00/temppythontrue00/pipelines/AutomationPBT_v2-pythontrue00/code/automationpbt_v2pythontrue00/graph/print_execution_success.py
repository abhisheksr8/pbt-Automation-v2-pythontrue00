from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbt_v2pythontrue00.config.ConfigStore import *
from automationpbt_v2pythontrue00.functions import *

def print_execution_success(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print("Successfully Executed Son.")
    out0 = in0

    return out0
