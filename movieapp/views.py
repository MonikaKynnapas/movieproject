import urllib.parse
from urllib.request import urlopen
import json

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.conf import settings
from .models import *

# Create your views here.
class HomeView(TemplateView):
    template_name = 'movieapp/index.html'

class SearchView(TemplateView):
    template_name = 'movieapp/search.html'

class SearchResultView(ListView):
    model = Country
    template_name = 'movieapp/search_result.html'
    table = None  # (country, movie, None)


    def get_queryset(self):
        object_list = []
        # form input:text->name="search"
        query = self.request.GET.get("search")
        # form select:name= 'table'
        self.table = self.request.GET.get("table")

        if self.table == 'country':
            # search from table of country
            object_list = Country.objects.filter(common__icontains=query)
        elif self.table == 'movie':
            value = urllib.parse.quote_plus(query)
            search = 's=' + value  # what search
            result = '&'.join([settings.OMDB_URL, search])
            print(result)
            response = urlopen(result)
            data = json.loads(response.read())
            if data['Response'] == 'True':
                for obj in data['Search']:
                    object_list.append(obj)
                    Movie.objects.get_or_create(title=obj['Title'], year=obj['Year'], imdb=obj['imdbID'],
                                                type=obj['Type'], poster=obj['Poster'])

        return object_list  # return search result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.table
        return context