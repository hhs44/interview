from rest_framework import serializers

from app.models import Grade, Students, Teachers


# 学生信息
class StudentSimpleSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()

    @staticmethod
    def get_sex(teacher):
        return "男" if teacher.sex else "女"

    @staticmethod
    def get_grade(student):
        return student.cls.grade_name

    class Meta:
        model = Students
        fields = ("id", "name", "sex", "age", "memo", "grade")


# 创建学生的信息
class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


# 老师信息
class TeacherSimpleSerializer(serializers.ModelSerializer):
    sex = serializers.SerializerMethodField()

    @staticmethod
    def get_sex(teacher):
        return "男" if teacher.sex else "女"

    class Meta:
        model = Teachers
        fields = ("teacherid", "name", "sex", "age", "memo", "grades")


# 班级信息
class GradeSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"


# 班级信息加学生老师人数信息
class GradeDetailSerializer(serializers.ModelSerializer):
    # 创建学生数量和老师数量
    count_s = serializers.SerializerMethodField()
    count_t = serializers.SerializerMethodField()

    @staticmethod
    def get_count_s(grade):
        queryset = Students.objects.filter(cls=grade.gradeid)
        return len(StudentSimpleSerializer(queryset, many=True).data)

    @staticmethod
    def get_count_t(grade):
        queryset = Teachers.objects.filter(grades=grade.gradeid)
        return len(TeacherSimpleSerializer(queryset, many=True).data)

    class Meta:
        model = Grade
        fields = ('gradeid', 'grade_name', 'count_s', "count_t")
