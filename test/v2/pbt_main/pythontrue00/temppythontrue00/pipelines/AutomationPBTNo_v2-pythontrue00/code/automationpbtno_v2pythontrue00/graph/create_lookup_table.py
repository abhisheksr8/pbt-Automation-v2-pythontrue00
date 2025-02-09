from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automationpbtno_v2pythontrue00.config.ConfigStore import *
from automationpbtno_v2pythontrue00.functions import *

def create_lookup_table(spark: SparkSession, in0: DataFrame):
    keyColumns = ['''customer_id''', '''email''']
    valueColumns = ['''country_code''']
    createLookup("LookupTest", in0, spark, keyColumns, valueColumns)
