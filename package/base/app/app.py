from package.base.nacos import NacosClient
from package.base.apollo import ApolloClient
import re
from datetime import datetime


from flask import Flask, Blueprint

webapp = Flask(__name__)

commonBp = Blueprint('kpi', __name__)

NACOS_SERVER_ADDRESSES = "127.0.0.1:8848"
NACOS_NAMESPACE = "public"
NACOS_SERVICE_NAME = "python.test.domain"
NACOS_INSTANCE_IP = "127.0.0.1"
NACOS_INSTANCE_PORT = "5000"


APOLLO_APP_ID = "SampleApp"
APOLLO_SERVER_URL = "http://localhost:8080"

nacosClient = NacosClient(NACOS_SERVER_ADDRESSES, NACOS_SERVICE_NAME,
                          NACOS_INSTANCE_IP, NACOS_INSTANCE_PORT, NACOS_NAMESPACE)
apolloClient = ApolloClient(
    app_id=APOLLO_APP_ID, config_server_url=APOLLO_SERVER_URL)

# 暂时不需要start
# apolloClient.start()
