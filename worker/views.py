from django.db.models import QuerySet, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import FormView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WorkerSerializer
from .models import Worker
from .seeder import seeder_setup


@api_view(['GET'])
def db_setup(request):
    seeder_setup()
    return Response({'ok':True})


@api_view(['GET'])
def workers(request):
    directors = Worker.objects.filter(post='Директор')

    json_directors = []

    for director in directors:
        json_director = worker_to_json(director)
        json_directors.append(json_director)

    return Response({'directors': json_directors})


def worker_to_json(worker):
    data = {
        'full_name': worker.full_name,
        'employment_date': worker.employment_date,
        'post': worker.post,
        'salary': worker.salary,
        'subjects': []
    }

    for subject in worker.subjects.all():
        data['subjects'].append(worker_to_json(subject))

    return data


class WorkerViewSet(ListAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        params = self.request.query_params

        if 'search' in params:

            qs = Worker.objects.filter(Q(full_name__icontains=params['search'])) \
                | Worker.objects.filter(Q(employment_date__icontains=params['search'])) \
                | Worker.objects.filter(Q(post=params['search'])) \
                | Worker.objects.filter(Q(salary__icontains=params['search']))
            # qs = qs | qs.filter(chief__icontains = params['search'])


        if 'sort' in params:
            qs = qs.order_by(params['sort'])

        return qs


class WorkerCreateView(CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = [IsAuthenticated]


class WorkerRetrieveView(RetrieveAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = [IsAuthenticated]


class WorkerUpdateView(UpdateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = [IsAuthenticated]


class WorkerDestroyView(DestroyAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
    permission_classes = [IsAuthenticated]


class LoginPage(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/api/list/'

    def form_valid(self, form):
        super().form_valid(form)
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

