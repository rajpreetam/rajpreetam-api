from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Blog, Category, Tag
from .serializers import BlogSerializer


class BlogView(APIView):
    def get(self, request):
        try:
            blog = Blog.objects.all()
            serializer = BlogSerializer(blog, many=True)
            return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Blogs fetched successfully',
                'data': serializer.data,

            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'success': False,
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Something went wrong',
                'data': None,
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

