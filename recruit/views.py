from django.shortcuts import get_object_or_404  # 모델 객체가 없으면 404에러 발생시키기 위함
from rest_framework.response import Response
from .models import JobPosting
from .serializers import JobPostingModelSerializer, JobPostingCreateSerializer, JobPostingUpdateSerializer
from rest_framework import status
from rest_framework.views import APIView  # APIView를 이용



# 채용공고 전체 목록 조회 View - 채용공고 등록 View
class JobPostingsAPIView(APIView):
    # GET 방식일 때는 채용공고 전체 목록 조회
    def get(self, request):
        jobpostings = JobPosting.objects.all()
        serializer = JobPostingModelSerializer(jobpostings, many=True)  # 단일 객체가 아닌 객체 목록을 serializer 하기 위해 many=True 설정

        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST 방식일 때는 채용공고 등록
    def post(self, request):
        serializer = JobPostingCreateSerializer(data=request.data)  # 입력된 data 보내기
        if serializer.is_valid():  # 유효성 검증 후 통과하면 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 검증되지 않는 경우 400 예외처리


# 채용공고 상세 조회 View - 채용공고 수정 View - 채용공고 삭제 View
class JobPostingDetailAPIView(APIView):
    # GET 방식일 떄는 채용공고 상세 조회
    def get(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)  # 모델 객체가 없으면 404 예외처리
        serializer = JobPostingDetailSerializer(jobposting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # PUT 방식일 때는 채용공고 수정
    def put(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)
        serializer = JobPostingUpdateSerializer(jobposting, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE 방식일 때는 채용공고 삭제
    def delete(self, request, pk):
        jobposting = get_object_or_404(JobPosting, id=pk)
        jobposting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
