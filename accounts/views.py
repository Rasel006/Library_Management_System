from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from book.models import Bookpurchase
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        # Save user registration form and login the user
        user = form.save()
        login(self.request, user)
        
        # Display success message
        messages.success(self.request, "After registration, Login successfully")
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        # Display success message
        messages.success(self.request, "Login successfully")
        return reverse_lazy('home')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        # Logout the user, display success message, and redirect to home
        if self.request.user.is_authenticated:
            logout(self.request)
        messages.success(self.request, "Logout successfully")
        return reverse_lazy('home')

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'accounts/profile.html'
    # Note: 'balance' is defined as a class attribute. Consider moving it inside a method if it's dynamic.

    def get(self, request):
        # Get user purchases and account balance
        user_purchases = Bookpurchase.objects.filter(user=request.user)
        account_balance = request.user.account.balance

        # Create form for updating user profile
        form = UserUpdateForm(instance=request.user)

        # Render the profile page with relevant data
        return render(request, self.template_name, {
            'user_purchases': user_purchases,
            'account_balance': account_balance,
            'form': form,
        })

    def post(self, request):
        # Process form submission for updating user profile
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        
        # If form is not valid, re-render the profile page with errors
        user_purchases = Bookpurchase.objects.filter(user=request.user)
        account_balance = request.user.account.balance
        return render(request, self.template_name, {'user_purchases': user_purchases, 'account_balance': account_balance, 'form': form})
