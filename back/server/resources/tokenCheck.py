
# todo 验证登录状态是否有效

from flask.ext import restful
from flask.ext.restful import reqparse
from ..models import Users
import hashlib
import time
import base64
import hmac

secretKey = 'JD98Dskw=23njQndW9D'
maxAge = 10


class TokenCheck(restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str, required=True, help='username is required', location='form')
        args = parser.parse_args()
        tokenArr = args['token'].split('-')
        user = Users.query.filter_by(id=tokenArr[0]).first()
        if time.time() < float(tokenArr[1]):
            s = '%s-%s-%s-%s' % (user.id, user.password, tokenArr[1], secretKey)
            if hashlib.sha1(s.encode('utf-8')).hexdigest() == tokenArr[2]:
                return 'success'
        return 'fail'

