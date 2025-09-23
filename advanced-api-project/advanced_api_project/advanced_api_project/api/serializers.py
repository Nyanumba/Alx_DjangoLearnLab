from rest_framework import serializers
from api.models import Book,  Author
import datetime

#serializer class for the book model
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]

#validation

def validate_publication_year(self, value):
    current_year = datetime.date.today().year
    if value > current_year:
        raise serializers.ValidationError("The publication date cannot be from the future, it must be present date or past")
    return value

#nested book serializer class
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializers(many = True, read_only = True)
    
    class Meta:
        model = Author
        fields = ["id", "name", "books"]
        
        