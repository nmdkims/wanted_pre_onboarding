from django.db import models
from user.models import User


# user 모델은 custom user 모델을 사용

# 회사
class Company(models.Model):
    name = models.CharField('회사명', max_length=50)
    country = models.CharField('국가', max_length=20)
    region = models.CharField('지역', max_length=20)

    def __str__(self):
        return self.name


# 채용공고
class JobPosting(models.Model):
    # 회사가 사라지면 해당 회사가 작성한 포스팅이 사라져야 하기 때문에 CACADE 옵션 적용
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_jobposting',
                                verbose_name='회사_id', null=True)
    # User 모델과 다대다 관계 설정 해당  내용은 6번내용인 채용공고에 지원에서 사용할 예정
    applicant = models.ManyToManyField(User, verbose_name='지원자', blank=True)

    position = models.CharField('채용포지션', max_length=100)
    reward = models.IntegerField('채용보상금', default=0)
    description = models.TextField('채용내용')
    tech_stack = models.CharField('사용기술', max_length=100)

    def __str__(self):
        return self.company
