import boto3
from sagemaker import Session
from sagemaker.model import Model
from sagemaker import get_execution_role

# AWS and SageMaker Configurations
role = "arn:aws:iam::145023121577:role/sudhirsagemakerrole"
region = "us-east-1"
ecr_image_uri = "145023121577.dkr.ecr.us-east-1.amazonaws.com/sudhirecr:latest"
# s3_input_path = "s3://your-s3-bucket/input/test_data.csv"
# s3_output_path = "s3://your-s3-bucket/output/"

# Initialize a SageMaker Session
sagemaker_session = Session(boto3.Session(region_name=region))

# Create a SageMaker Model using the custom ECR image
model = Model(
    image_uri=ecr_image_uri,
    role=role,
    sagemaker_session=sagemaker_session,
)

# Deploy the model to a SageMaker endpoint
predictor = model.deploy(
    instance_type="ml.m4.4xlarge",  
    initial_instance_count=1  # The number of instances for the endpoint
)