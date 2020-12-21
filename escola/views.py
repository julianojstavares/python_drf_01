from django.db.models import query
from rest_framework import viewsets, generics
from escola.models import Curso, Aluno, Matricula
from escola.serializer import AlunoSerializer
from escola.serializer import CursoSerializer
from escola.serializer import MatriculaSerializer
from escola.serializer import ListaMatriculasAlunoSerializer
from escola.serializer import ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os alunos """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibe todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """ Exibe todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """ Exibe todas as matriculas de um aluno """

    def get_queryset(self):
        querySet = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return querySet
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """ Exibe todos os alunos matriculados em um determinado curso """

    def get_queryset(self):
        querySet = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return querySet
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
