# Django REST framework Serializer

## Basic

Object -> Dict
```py
serializer = CommentSerializer(comment)
serializer.data
```

Validation
```py
serializer = CommentSerializer(data=data)
serializer.is_valid()
serializer.validated_data
# {...}
```

raise error
```py
serializer.is_valid(raise_exception=True)
```

## Custom Serializer

### 応用 1 Model Serializer
```py
class CompanySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    code = serializers.CharField(required=False)
    name = serializers.CharField()

# write_only もあり

class CompanyListSerializer(serializers.Serializer):
    companies = CompanySerializer(many=True)

# {'companies': [{'id': ..., 'code': ..., 'name': ...}, ...]}

class CompanyItemSerializer(serializers.Serializer):
    company = CompanySerializer(many=False)

# {'company': {'id': ..., 'code': ..., 'name': ...}}

class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('id', )
```

### 応用 2 メソッドの上書き

```py
class ASerializer(serializers.ModelSerializer):
    done = serializers.SerializerMethodField()
    as_sample = serializers.BooleanField(required=False)

    @classmethod
    def get_done(cls, instance):
        return instance.assignment.done

    def validate_name(self, value):
        try:
            ......
        except NameError:
            raise ....
        return value

    class Meta:
        model = A
        fields = ('id', 'text','meta', 'approver', 'name', 'date', 'class', 'done')


class SomeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = SomeModel
        fields = '__all__'

    def create(self, validated_data):
        .....
        obj.save()
        return obj

    def save(self, obj):
        .....
        obj.save()
        return obj

```


## その他

```py
from restframework import serializer
class CustomSerializer(serializer.Serializer):
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance
```