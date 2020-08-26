import datetime

# import jwt
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import Teachers, Students, Grade
from app.serializers import TeacherSimpleSerializer, StudentSimpleSerializer, GradeSimpleSerializer, \
    GradeDetailSerializer, StudentCreateSerializer, TeacherCreateSerializer
# 登录接口
from simpledemo.settings import SECRET_KEY


#
# @api_view(('POST',))
# def login(request):
#     username = request.data.get('username')
#
#     teacher = Teachers.objects.filter(name=username).first()
#     if teacher:
#         payload = {
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
#             'data': {
#                 'teacherid': teacher.id
#             }
#         }
#         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode()
#         return Response(data={'token': token})
#     return Response(data={"msg": "用户不存在！"})


class TeacherView(ModelViewSet):
    """
    老师视图
    """
    queryset = Teachers.objects.all()
    serializer_class = TeacherSimpleSerializer


class StudentView(ModelViewSet):
    """
    学生视图
    """
    queryset = Students.objects.all()
    serializer_class = StudentSimpleSerializer

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return StudentCreateSerializer
        return StudentSimpleSerializer


class GradeView(ModelViewSet):
    """
    班级视图
    """
    queryset = Grade.objects.all()

    def get_serializer_class(self):
        if self.action in ('list',):
            return GradeDetailSerializer
        return GradeSimpleSerializer
