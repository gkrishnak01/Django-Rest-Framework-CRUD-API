from django.shortcuts import render
from .models import ToDo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.


"""Function Based Views"""

@api_view(["GET","POST"])
def createReadTodoFunction(request):
    if(request.method == "GET"):
        todos = ToDo.objects.all()
        serializer = TodoSerializer(todos,many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if(request.method == "POST"):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(["PUT","GET","DELETE"])
def individualTodoFunction(request,id):

    try:
        todo = ToDo.objects.get(pk = id)
    except:
        return Response(status = status.HTTP_400_BAD_REQUEST)

    if(request.method == "PUT"):
        serializer = TodoSerializer(todo,request.data)
        if serializer.is_valid():
            serializer.saveDELETE()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if(request.method == "GET"):
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if(request.method == "DELETE"):
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Class Based Views"""

class CreateReadToDoClass(APIView):

    def get(self,request):
        todos = ToDo.objects.all()
        serializer = TodoSerializer(todos,many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self,request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)



class IndividualToDoClass(APIView):

    def getTodo(self,id):
        try:
            todo = ToDo.objects.get(pk = id)
            return todo
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        todo = self.getTodo(id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self,request,id):
        todo = self.getTodo(id)
        serializer = TodoSerializer(todo,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        todo = self.getTodo(id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

"""Using Mixins"""

class ToDoMixins(generics.GenericAPIView, 
                mixins.ListModelMixin, 
                mixins.CreateModelMixin, 
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):

 
    lookup_field = "id"
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

    def get(self,request,id = None):
        if id:
            return self.retrieve(request,id)
        return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id):
        return self.update(request)

    def delete(self,request,id):
        return self.destroy(request)










  

    
        
            



        


    
    
