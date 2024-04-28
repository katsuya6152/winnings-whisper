FROM public.ecr.aws/lambda/python:3.11

# lightgbmをインストールするために
RUN yum install -y gcc-c++ make

COPY requirements.txt  .
RUN  pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY train.py ${LAMBDA_TASK_ROOT}

CMD [ "train.handler" ]