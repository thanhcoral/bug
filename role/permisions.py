from django.http import Http404

from rest_framework import exceptions
from rest_framework.permissions import BasePermission


class ViewStudentList(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated
        )