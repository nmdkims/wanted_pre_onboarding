from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Company, JobPosting


# 회사와 관련된 Serializer - 채용공고 전체 목록 조회 Serializer와 연결
class CompanySerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화
    회사명 = serializers.CharField(source='name')
    국가 = serializers.CharField(source='country')
    지역 = serializers.CharField(source='region')

    class Meta:
        model = Company
        fields = ('회사명', '국가', '지역')


# 채용공고 전체 목록 조회 Serializer
class JobPostingModelSerializer(serializers.ModelSerializer):
    # model에 정의한 필드 이름을 한글화
    채용공고_id = serializers.IntegerField(source='id')
    채용회사 = serializers.IntegerField(source='company_id')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='tech_stack')

    class Meta:
        model = JobPosting
        fields = ('채용공고_id', '채용회사', '채용포지션', '채용보상금', '사용기술')


# 채용공고 등록
class JobPostingCreateSerializer(serializers.ModelSerializer):
    회사_id = serializers.IntegerField(source='company_id')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='description')
    사용기술 = serializers.CharField(source='tech_stack')

    class Meta:
        model = JobPosting
        fields = ('회사_id', '채용포지션', '채용보상금', '채용내용', '사용기술')


# 채용공고 수정
class JobPostingUpdateSerializer(serializers.ModelSerializer):
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    채용내용 = serializers.CharField(source='description')
    사용기술 = serializers.CharField(source='stack')

    class Meta:
        model = JobPosting
        fields = ('채용포지션', '채용보상금', '채용내용', '사용기술')  # 회사_id는 그대로 사용


# 채용공고 상세 조회 Serializer
class JobPostingDetailSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.IntegerField(source='id')
    채용회사 = serializers.IntegerField(source='company_id')
    채용포지션 = serializers.CharField(source='position')
    채용보상금 = serializers.IntegerField(source='reward')
    사용기술 = serializers.CharField(source='tech_stack')
    채용내용 = serializers.CharField(source='description')  # 채용내용 필드

    class Meta:
        model = JobPosting
        fields = ('채용공고_id', '채용회사', '채용포지션', '채용보상금', '사용기술', '채용내용')
