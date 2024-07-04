# ClickStream Data Pipeline
![clickstream](https://github.com/HossamHeikal/clickstream-data-pipeline/assets/58578405/e0986e70-c7cd-4083-8178-b3e15e0810ba)

## Steps to create the pipeline

1. **Create an S3 bucket**
   - On AWS, create an S3 bucket with the name `clickstream-ingest`.

2. **Upload project content**
   - Upload all the content in the project's folder to the S3 bucket.

3. **Set up CloudFormation**
   - Open CloudFormation and create a new stack.
   - Paste the S3 YAML file URL located in the cloudformation folder on S3.

4. **Launch the stack**
   - Create the stack and wait for the services to launch.

5. **Create a Visual ETL in AWS Glue**
   - Go to AWS Glue and create a Visual ETL.
   - Choose to upload and select the `Ingest.json` file. This will visually show how the ETL process works.

6. **Create a Spark script in AWS Glue**
   - In AWS Glue, create a Spark script and upload the `Transform.json` file.

7. **Run the metadata crawler**
   - Navigate to the `metadata_crawler` and run a crawl. This will create the tables used for enrichment.

8. **Configure the Ingest Job**
   - Navigate to the Ingest Job and make sure all the joins are working correctly.

9. **Test the Lambda Producer function**
   - Navigate to Lambda, then inside the Producer function, click test then invoke. The raw enriched data will start to be saved in S3 in Parquet format.

10. **Run the Transform job**
    - Navigate to the Transform job and run it to test the results. Schedule the job to run hourly.

11. **Run the clickstream crawler**
    - Run the clickstream crawler to be able to query the data in AWS Athena.

> **Note:** AWS Glue is not included in the AWS Free Tier.
