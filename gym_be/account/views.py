from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import SerializeRegister, SerializeListUser

User = get_user_model()


class RegisterView(GenericAPIView):
	serializer_class = SerializeRegister

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data, status=201)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_list_view(request, *args, **kwargs):
	"Lists all users on the system"
	qs = User.objects.all()
	serializer = SerializeListUser(qs, many=True)
	return Response(serializer.data, status=200)
