from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import OrderModelForm
from users.models import AccountModel
from .models import OrderItemModel
from django.contrib.auth.decorators import login_required

class CheckoutView(TemplateView):
    template_name = 'product-checkout.html'

@login_required
def order_create(request):
    if request.method == 'POST':    
        form = OrderModelForm(request.POST)
        if form.is_valid():
            account = AccountModel.objects.get(user=request.user) 
            unew_order = AccountModel.objects.get(user=request.user, status=False)
            cart = request.session.get('cart', None)
            if cart  is None:
                return redirect('product:list')
            products = ProductModel.objects.filter(id__in=cart)
            for product in products:
                OrderItemModel.objects.create(
                    product=product,
                    quantity=1,
                    size='test',
                    price=product.real_price,
                    order=new_order,
                    image1=product.image1,
                    image2=product.image2
                )
            request.session['cart'] = []
            return redirect('product:list')
        else:
            return render( request, 'product-checkout.html')

class OrderView(LoginRequiredMixin, CreateView):
    template_name = 'product-checkout.html'
    from_class = OrderModelForm
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('product:list')

    def from_valid(self, form):
        print(form.cleaned_data)
    
    def from_invalid(self, form):
        print(form.errors)
