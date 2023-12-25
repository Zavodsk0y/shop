from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from .forms import *


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'


class ProductsListView(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.GET.get('search_query')

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm(self.request.GET)
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'


class UserProfileView(ListView):
    model = OrderedProduct
    template_name = 'profile.html'
    context_object_name = 'products'

    def get_queryset(self):
        return OrderedProduct.objects.filter(user=self.request.user)




@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user
    ordered_item = OrderedProduct.objects.create(user=user, product=product)

    return HttpResponseRedirect('/')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('create_product')


class BBLogoutView(LogoutView):
    template_name = 'registration/logout.html'
