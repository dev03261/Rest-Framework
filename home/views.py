from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response  import Response
from .models import *
from .serializers import*
from rest_framework import status
#in case of APIs we cannot return html
# Create your views here.
#def home(request):
  #  return render(request,'index.html')


#for this we use decorator

#here when we will use get in thunderstron will receive an error like this
#  "detail": "Method \"GET\" not allowed."

# @api_view(['GET'])
# def home(request):
#     student_objs=Student.objects.all()
#     serializer=StudentSerializer(student_objs,many=True)
#     return Response({'status':200,'payload':serializer.data})



# @api_view(['POST'])
# def home2(request):
#     data = request.data  # Get the data from the request

#     # Create a new student object using the serializer
#     serializer = StudentSerializer(data=data)
#     #we can do custom validations as well
#     #if request.data['age']<18:
#        #return Response({'status':403},'message':'age is less than 18')
#     if 'first_name' in data and any(char.isdigit() for char in data['first_name']):
#         return Response({'status': 403, 'message': 'Name cannot contain digits'})
#     if serializer.is_valid():
#         serializer.save()  # Save the student object to the database
#         return Response({'status': 200, 'message': 'You have created data successfully'})
#     else:
#         return Response({'status': 400, 'message': 'Invalid data'})


# @api_view(['PUT'])
# def update_student(request, id):
#     try:
#         student = Student.objects.get(pk=id)
#     except Student.DoesNotExist:
#         return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Student not found'})
#     data = request.data
#     serializer = StudentSerializer(student, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'status': status.HTTP_200_OK, 'message': 'Student updated successfully'})
#     else:
#         return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Invalid data'})



# @api_view(['DELETE'])
# def delete_student(request,id):
#     try:
#         student = Student.objects.get(pk=id)
#     except Student.DoesNotExist:
#         return Response({'status': 404, 'message': 'Student not found'})

#     student.delete()
#     return Response({'status': 200, 'message': 'Student deleted successfully'})


class studentAPI(APIView):

    def get(self,request):
      student_objs=Student.objects.all()
      serializer=StudentSerializer(student_objs,many=True)
      return Response({'status':200,'payload':serializer.data})

    def post(self,request):
      serializer = StudentSerializer(data= request.data)

      if serializer.is_valid():
         serializer.save()  # Save the student object to the database
         return Response({'status': 200, 'message': 'You have created data successfully'})
      else:
         return Response({'status': 400, 'message': 'Invalid data'})


    def put(self,request):
     try:
           student = Student.objects.get(pk=id)
     except Student.DoesNotExist:
        return Response({'status': status.HTTP_404_NOT_FOUND, 'message': 'Student not found'})

     data = request.data
     serializer = StudentSerializer(student, data=data)

     if serializer.is_valid():
        serializer.save()
        return Response({'status': status.HTTP_200_OK, 'message': 'Student updated successfully'})
     else:
        return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Invalid data'})


    def patch(self,request):
        pass

    def delete(self,equest):
        pass
