from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy #metodo que ira permitir usar a rota com o apelido dela(nome que criou para a rota).

from datetime import date
from django.shortcuts import redirect

# Create your views here. // Crie suas visualizações aqui.
def home(request):
    #return HttpResponse('<h1>bem vindo a sua primeira aplicação do Reginaldo Silva</h1>')
      return render(request, 'todos/home.html')

#baseada em função:
'''
def todoListar(request):
     # tarefas = [{
    #     'id':'1',
    #     'Tarefa':'comprar fraldas'
    # }]

    tarefas = Todo.objects.all()  # busca todos os dados do banco

    return render(request, "todos/todolistar.html",{'tarefas':tarefas})
''' 
class todoListarView(ListView):
    model = Todo #classe deve usar o modelo ToDo (.\todos\models.py)

class todoCriarView(CreateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Adicionar Tarefa'
        return context

class todoAtualizarView(UpdateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Tarefa'
        return context
    
class todoDeletarView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_listar')

class todoCompletarView(View):
    def get(self,request,pk):
        tarefa = Todo.objects.get(pk=pk)
        tarefa.dtFinalizado = date.today()
        tarefa.save()
        return redirect('todo_listar')