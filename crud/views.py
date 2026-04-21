from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
class TopView(TemplateView):
    # templateフォルダからの相対パスを指定する。
    template_name="top.html"
    
class ProductListView(ListView,LoginRequiredMixin):
    model = Product
    # 1ページに表示する数を指定
    paginate_by = 3
    
class ProductCreateView(CreateView,LoginRequiredMixin):
    model = Product
    # 全フィールドを対象として指定
    fields = '__all__'
    
class ProductUpdateView(UpdateView,LoginRequiredMixin):
    model = Product
    fields = '__all__'
    # Template名の末尾を指定
    template_name_suffix = '_update_form'
    
class ProductDeleteView(DeleteView,LoginRequiredMixin):
    model = Product
    success_url = reverse_lazy('list')
    
class Loginview(LoginView):
    form_class = AuthenticationForm
    # templateファイルの指定
    template_name = 'login.html'
    
class Logoutview(LogoutView):
    template_name = 'top.html'