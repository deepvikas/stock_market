from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Stock
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

import logging
_logger = logging.getLogger(__name__)


def home(request):
    return render(request, 'stock/details.html')


class StockDetailView(DetailView):
    model = Stock

class StockCreateView(LoginRequiredMixin, CreateView):
    model = Stock
    fields = ['title', 'name', 'price']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def details(request):
    context = {
        'stocks': Stock.objects.all()[0:5],
        'total_obj' : Stock.objects.count()
    }
    return render(request, 'stock/details.html', context, )

def loadmore(requset):
    total_item = int(requset.GET.get('total_item'))
    limit = 5
    stock_obj = list(Stock.objects.values()[total_item:total_item+limit])
    data = {
        'stocks': stock_obj,
        'total_obj_length' : Stock.objects.count()
    }
    return JsonResponse(data=data)

def showless(requset):
    total_item = int(requset.GET.get('total_item'))
    limit = 5
    end = (total_item-1) // limit
    _logger.error("- -- -- -  %r ------"%total_item)
    _logger.error("- -- -- -  %r ------"%(end*limit))
    stock_obj = list(Stock.objects.values())[total_item:(end*limit)-1:-1]
    data = {
        'stocks': stock_obj 
    }
    _logger.error("- -- -- -  %r ------"%data)
    return JsonResponse(data=data)
