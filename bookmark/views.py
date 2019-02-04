from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# view 두 종류 : 함수형, 클래스형
# 장고 목적? : 귀찮은거 하기 싫어서....
# 클래스형 : 자주 쓰는 기능을 상속받아서 간단하게 생성

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView

# list view
from .models import Bookmark
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 렌더링할 템플릿 파일이 지정이 되어있습니다.
    # bookmark/bookmark_list.html
    paginate_by = 3

from django.urls import reverse_lazy

class BookmarkCreateView(CreateView):
    model = Bookmark #입력화면에 출력된 form tag를 자동으로 만들어줌
    # _form : create, update
    # default : _form
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name','url']
    # get_absolute_url
    success_url =  reverse_lazy('list')


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark