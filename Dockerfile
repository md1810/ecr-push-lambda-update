FROM public.ecr.aws/lambda/python:3.8

RUN yum install libgomp -y

# Copy function code
COPY app.py .
COPY requirements.txt  .

RUN  pip3 install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]