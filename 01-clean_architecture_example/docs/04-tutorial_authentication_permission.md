# Authenticator/Permission

## 定義
### Authentication
```py
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
class SomeAuthentication(BaseAuthentication):
    ....
    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        ....
        return (user, auth)
```

### Permission
```py
from rest_framework.permissions import BasePermission
import setttings
class SomePermission(BasePermission):
    def has_permission(self, request, view):
        secret = self.get_password_from_head(request)
        return secret == settings.BACKEND_ENCRYPTION
```

## 使用箇所
viewset に入れる
```py
class ExampleView(ViewSet):
    authentication_classes = [SomeAuthentication]
    permission_classes = [IsAuthenticated]
```


settings にてデフォルトも設定可能
```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'somedirectory.SomeAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'somedirectory.IsBackend',
    ),
}
```