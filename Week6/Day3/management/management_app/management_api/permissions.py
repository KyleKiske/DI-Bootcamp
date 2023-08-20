from rest_framework.permissions import BasePermission

class IsDepartmentAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'DELETE']:
            return request.user == obj.administrator