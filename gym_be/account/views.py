from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import SerializeRegister, SerializeListUser
User = get_user_model()


class RegisterView(GenericAPIView):
	serializer_class = SerializeRegister

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=HTTP_201_CREATED)


@api_view(['GET'])
def users_list_view(request, *args, **kwargs):
	"""Lists all users on the system"""
	qs = User.objects.all().order_by('-created')
	serializer = SerializeListUser(qs, many=True)
	return Response(serializer.data, status=HTTP_200_OK)


class UserListView(ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all()
	serializer_class = SerializeListUser
	# permission_classes = [permissions.IsAuthenticated]
