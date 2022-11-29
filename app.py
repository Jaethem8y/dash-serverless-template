"""
Template for deploying Dash app using serverless framework
https://stackoverflow.com/questions/66845303/deploying-a-plotly-dash-app-to-aws-using-serverless-framework
https://medium.com/swlh/developing-a-serverless-backend-api-using-flask-39398d0eb95d
https://stackoverflow.com/questions/45342990/aws-lambda-error-unzipped-size-must-be-smaller-than-262144000-bytes
https://github.com/serverless/serverless-python-requirements/issues/663
https://github.com/99x/serverless-dynamodb-local/issues/135
https://stackoverflow.com/questions/66845303/deploying-a-plotly-dash-app-to-aws-using-serverless-framework
https://stackoverflow.com/questions/53220719/importerror-no-module-named-dash
https://www.serverless.com/blog/flask-serverless-api-in-aws-lambda-the-easy-way
https://github.com/plotly/dash/issues/22 
"""

from collections import namedtuple
import dash
from flask import Flask
import pkg_resources

_true_get_distribution = pkg_resources.get_distribution
_Dist = namedtuple('_Dist', ['version'])

def _get_distribution(dist):
    if dist == 'flask-compress':
        return _Dist('1.9.0') # your flask-compress version
    else:
        return _true_get_distribution(dist)

pkg_resources.get_distribution = _get_distribution

server = Flask(__name__)

app = dash.Dash(__name__,
                server=server,
                routes_pathname_prefix='/',
                requests_pathname_prefix='/dev/'
                )

"""
  put your dash logic here
"""
def __call__(self, *args, **kwargs):
    return self.server.__call__(*args, **kwargs)

if __name__ == '__main__': 
    server.run(debug=True, port = 8000)
