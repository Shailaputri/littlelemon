from rest_framework import serializers
from restaurant.models import Menu, BookingTable, Category, Rating
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from django.contrib.auth.password_validation import validate_password

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id', 'title']
		# fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
	category_id = serializers.IntegerField(write_only = True)
	category = CategorySerializer(read_only = True)
	class Meta:
		model = Menu
		fields = ['id','title', 'price', 'inventory', 'description', 'category', 'category_id']
		# fields = ['title', 'price', 'inventory', 'description', 'category']
		fields = '__all__'
		extra_kwargs = {
		'price' : {'min_value' : 2}, 
		'inventory' : {'min_value' : 0}
		}


class BookingTableSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookingTable
		fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
	'''
	Serializer that allows only 1 rating for 1 user per menu item
	'''
	user = serializers.PrimaryKeyRelatedField(
		queryset = User.objects.all(),
		default = serializers.CurrentUserDefault()
		)
	class Meta:
		model = Rating
		fields = ['user', 'menuitem_id', 'rating']
		validators = [UniqueTogetherValidator(queryset=Rating.objects.all(),\
		fields = ['user','menuitem_id','rating'])]
		extra_kwargs = {
		'rating' : {'max_value' : 5, 'min_value' : 0}}


		







class RegisterSerializer(serializers.ModelSerializer):
	username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)
	class Meta:
		model = User
		fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
		extra_kwargs = {
		    'first_name': {'required': True},
		    'last_name': {'required': True}
		}
		
	def validate(self, attrs):
	    if attrs['password'] != attrs['password2']:
	        raise serializers.ValidationError({"password": "Password fields didn't match."})

	    return attrs

	def create(self, validated_data):
	    user = User.objects.create(
	        username=validated_data['username'],
	        email=validated_data['email'],
	        first_name=validated_data['first_name'],
	        last_name=validated_data['last_name']
	    )

	    
	    user.set_password(validated_data['password'])
	    user.save()

	    return user
