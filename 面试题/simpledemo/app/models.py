from django.db import models


# Create your models here.
class PersonModel(models.Model):
    """人物基类"""
    # 姓名
    name = models.CharField("姓名", max_length=20)
    # 年龄
    age = models.IntegerField("年龄")
    # 性别
    sex = models.BooleanField("性别", default=True)
    # 备注
    memo = models.CharField("备注", max_length=255, default=None)

    class Meta:
        abstract = True


class Grade(models.Model):
    """班级"""
    # 班级ID
    gradeid = models.AutoField("班级编号", primary_key=True)
    # 班级名称
    grade_name = models.CharField("班级名称", max_length=20, unique=True)

    class Meta:
        db_table = "grade"
        verbose_name = "班级"
        verbose_name_plural = verbose_name


class Teachers(PersonModel):
    """老师"""
    # 老师ID
    teacherid = models.AutoField("老师编号", primary_key=True)
    # 老师的班级
    grades = models.ManyToManyField(to='Grade', through="TeachersGrade", default=None)

    class Meta:
        db_table = "teachers"
        verbose_name = "老师"
        verbose_name_plural = verbose_name


class TeachersGrade(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='编号')
    grade = models.ForeignKey(to=Grade, on_delete=models.DO_NOTHING, db_column="gradeid")
    teacher = models.ForeignKey(to=Teachers, on_delete=models.DO_NOTHING, db_column="teacherid")

    class Meta:
        db_table = "teacher_grade"
        verbose_name = "老师班级"
        verbose_name_plural = verbose_name


class Students(PersonModel):
    """学生"""
    # 学生和班级的关系
    cls = models.ForeignKey(to=Grade, on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        db_table = "students"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
