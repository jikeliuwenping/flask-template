from package.base.nacos import NacosClient
from package.base.apollo import ApolloClient
import re
from datetime import datetime


from flask import Flask, Blueprint

webapp = Flask(__name__)

commonBp = Blueprint('kpi', __name__)

SERVER_ADDRESSES = "127.0.0.1:8848"
NAMESPACE = "public"
SERVICE_NAME = "python.test.domain"


nacosClient = NacosClient(SERVER_ADDRESSES, SERVICE_NAME, NAMESPACE)
apolloClient = ApolloClient(
    app_id="SampleApp", config_server_url="http://localhost:8080")

# 暂时不需要start
# apolloClient.start()
