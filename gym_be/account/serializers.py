from django.contrib.auth import get_user_model
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import CharField, ModelSerializer, \
	ValidationError

User = get_user_model()


class SerializeRegister(ModelSerializer):
	password = CharField(min_length=6, max_length=24, write_only=True)

	class Meta:
		model = User
		fields = ['email', 'username', 'password']

	def validate(self, attrs):
		email = attrs.get('email', '')
		username = attrs.get('username', '')

		if not username.isalnum():
			raise ValidationError(
				"Username should only contain alphanumeric characters"
			)

		return attrs

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)


class SerializeListUser(ModelSerializer):
	username = SerializerMethodField(read_only=True)

	class Meta:
		model = User
		fields = ['id', 'email', 'username', 'is_verified', 'is_active']

	# @staticmethod
	def get_username(self, obj):
		return obj
