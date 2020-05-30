from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import HttpResponse, request
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from leet.models import AnthemAsset, AnthemUser


class IndexView(TemplateView):
    template_name = 'index.html'


class AssetListView(ListView):
    paginate_by = 5
    model = models.AnthemAsset


class AssetDetailView(DetailView):
    context_object_name = 'asset_details'
    model = models.AnthemAsset
    template_name = 'leet/AnthemAsset_detail.html'



class AnthemUserListView(ListView):
    paginate_by = 5
    model = models.AnthemUser

class AnthemUserDetailView(DetailView):
    context_object_name = 'user_details'
    model = models.AnthemUser
    template_name = 'leet/AnthemUser_detail.html'

class AnthemUserCreateView(CreateView):
    model=models.AnthemUser
    fields = ('name','department','manager','internal_ext')

class AnthemUserDeleteView(DeleteView):
    model= models.AnthemUser
    success_url=reverse_lazy("leet:user_list")



class AnthemAssetCreateView(CreateView):
    model=models.AnthemAsset
    fields = ('asset_type','asset_number','asset_picture','description')

class AnthemAssetDeleteView(DeleteView):
    model = models.AnthemAsset
    success_url = reverse_lazy("leet:list")

class SearchResultsView(ListView):
    model = models.AnthemAsset
    template_name = 'leet/search_results.html'
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = AnthemAsset.objects.filter(
            Q(asset_number__icontains=query) | Q(anthem_user__name__icontains=query)
        )
        return object_list
    

#     def get_queryset(self):
#        result = super(SearchView, self).get_queryset()
#        query = self.request.GET.get('search')
#        if query:
#           postresult = AnthemAsset.objects.filter(title__contains=query)
#           result = postresult
#        else:
#            result = None
#        return result

