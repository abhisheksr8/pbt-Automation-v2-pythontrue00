from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from automationpbtno_v2pythontrue00.config.ConfigStore import *
from automationpbtno_v2pythontrue00.functions import *
from prophecy.utils import *
from automationpbtno_v2pythontrue00.graph import *

def pipeline(spark: SparkSession) -> None:
    df_s3_source_dataset = s3_source_dataset(spark)
    create_lookup_table(spark, df_s3_source_dataset)
    df_reformatted_customer_data = reformatted_customer_data(spark, df_s3_source_dataset)
    df_print_execution_success = print_execution_success(spark, df_reformatted_customer_data)
    df_select_from_temp_view = select_from_temp_view(spark, df_s3_source_dataset)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("AutomationPBT_v2-pythontrue00").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/AutomationPBTNo_v2-pythontrue00")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/AutomationPBTNo_v2-pythontrue00", config = Config)(
        pipeline
    )

if __name__ == "__main__":
    main()
