from core.models import (
    Tag,
    Ingredient,
    Recipe,
)

from rest_framework import serializers

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Ingredient
        fields = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for tags."""
    """Serializer for recipes."""
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Ingredient.objects.all()
    )   

    class Meta:
        model = Recipe
        fields = ['id', 'title','description', 'time_minutes', 'price', 'link', 'ingredients', 'tags']
        read_only_fields = ['id']

class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags= TagSerializer(many=True, read_only=True)

class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for tags."""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']
