from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import * #Grade, Subjects, Userprofile, Video
from .serializers import GradeSerializer, SubjectsSerializer, UserprofileSerializer, VideoSerializer

# Grade Views
@api_view(['GET', 'POST'])
def grade_list(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        grade_number = request.data.get('grade_number')
        term = request.data.get('term')
        print("----------------0")

        # Check if the grade and term combination already exists
        if Grade.objects.filter(grade_number=grade_number, term=term).exists():
            print("------------------1")
            return Response({"error": "This grade and term combination already exists."})

        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            print("----------------2")
            serializer.save()
            print("------------------3")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def grade_detail(request, pk):
    try:
        grade = Grade.objects.get(pk=pk)
    except Grade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GradeSerializer(grade)
        return Response(serializer.data)

    elif request.method == 'PUT':
        grade_number = request.data.get('grade_number')
        term = request.data.get('term')
        if Grade.objects.filter(grade_number=grade_number, term=term).exists():
            print("------------------1")
            return Response({"error": "This grade and term combination already exists so you cannot Edit."})
       
        serializer = GradeSerializer(grade, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        grade.delete()
        return Response({"message": "Grade deleted successfully."}, status=status.HTTP_200_OK)

# Subjects Views
@api_view(['GET', 'POST'])
def subjects_list(request):
    if request.method == 'GET':
        subjects = Subjects.objects.all()
        serializer = SubjectsSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectsSerializer(data=request.data)
        if serializer.is_valid():
            subject_name = serializer.validated_data['subject_name']
            grade_id = serializer.validated_data['grade'].id
            
            # Check if the subject already exists for the given grade
            if Subjects.objects.filter(subject_name=subject_name, grade_id=grade_id).exists():
                return Response(
                    {"error": "Subject with this name already exists for the given grade."})
            
            # If not, save the new subject
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def subjects_detail(request, pk):
    try:
        subject = Subjects.objects.get(pk=pk)
    except Subjects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubjectsSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectsSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subject.delete()
        return Response({"message": "Subject deletion accepted."}, status=status.HTTP_202_ACCEPTED)



# Userprofile Views
@api_view(['GET', 'POST'])
def userprofile_list(request):
    if request.method == 'GET':
        profiles = Userprofile.objects.all()
        serializer = UserprofileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserprofileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def userprofile_detail(request, pk):
    try:
        profile = Userprofile.objects.get(pk=pk)
    except Userprofile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserprofileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserprofileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response({"message": "User profile deleted successfully."}, status=status.HTTP_200_OK)

# Video Views
@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        video.delete()
        return Response({"message": "Video deleted successfully."}, status=status.HTTP_200_OK)
    

