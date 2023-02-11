from django.contrib.auth import login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import redirect
from accounts.forms import MyUserCreationForm, UserChangeForm, ProfileChangeForm
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.models import Profile
from django.contrib.auth import get_user_model


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:index')
        return next_url


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcements = self.object.author.all().exclude(status='deleted')
        # if self.request.user != self.object.author:
        #     announcements.fillter(status='published')
        context['announcements'] = announcements
        return context


class UserChangeView(PermissionRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'change.html'
    context_object_name = 'user_obj'
    form_profile_class = ProfileChangeForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserChangeView, self).get_context_data(**kwargs)
        if 'profile_form' not in kwargs:
            context['profile_form'] = self.form_profile_class(instance=self.get_object().profile)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        profile_form = self.form_profile_class(instance=self.get_object().profile, data=request.POST,
                                               files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        response = super().form_valid(form)
        profile_form.save()
        return response

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.get_object().pk})

    def has_permission(self):
        return self.get_object() == self.request.user


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.request.user.pk})

