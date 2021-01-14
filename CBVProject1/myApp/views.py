from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from myApp.models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student
    #default template = student_list.html
    #default context  = student_list
class StudentDetailView(DetailView):
    model = Student
    #default template = student_Detail.html
    #default context  = student
class StudentCreateView(CreateView):
    model = Student
    fields =("name","number","marks","place")
    #default template = student_form.html
class StudentUpadteView(UpdateView):
    model = Student
    fields = ('name','marks')
    #default template = student_form.html
class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    #default template = student_confirm_delete.html
