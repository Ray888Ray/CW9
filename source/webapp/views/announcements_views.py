from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.views import View

from webapp.models import Announcement, Comment
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import AnnouncementForm, CommentForm, ModerateAnnouncementForm
from django.shortcuts import reverse, get_object_or_404
from django.urls import reverse_lazy


class AnnouncementIndexView(ListView):
    template_name = 'announcements/index.html'
    context_object_name = 'announcements'
    model = Announcement
    paginate_by = 3

    def get_queryset(self):
        moderate = Announcement.objects.filter(status='published')
        return moderate


class AnnouncementView(DetailView):
    template_name = 'announcements/info.html'
    model = Announcement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        announcements = self.object
        announcements = announcements.announcements
        context['announcements'] = announcements.order_by('-created_at')
        context['form'] = CommentForm
        return context


class AnnouncementCreateView(CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/create.html'
    permission_required = 'webapp.add_announcement'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:info', kwargs={'pk': self.object.pk})


class AnnouncementUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AnnouncementForm
    template_name = 'announcements/update.html'
    model = Announcement
    permission_required = 'webapp.change_announcement'

    # def get_form_class(self):
    #     if self.request.user.has_perm('webapp.can_moderated'):
    #         return ModerateAnnouncementForm
    #     return AnnouncementForm
    #
    # def form_valid(self, form):
    #     if not self.request.user.has_perm('webapp.change_announcement'):
    #         form.instance.status = 'moderate'
    #     return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:info', kwargs={'pk': self.object.pk})


class AnnouncementDeletesView(PermissionRequiredMixin, DeleteView):
    template_name = 'announcements/delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_announcement'
    context_object_name = 'announcements'
    model = Announcement

    def form_valid(self, form):
        success_url = reverse_lazy('webapp:index')
        self.object.status = 'deleted'
        self.object.save()
        return HttpResponseRedirect(success_url)


class ListModeratedView(PermissionRequiredMixin, ListView):
    model = Announcement
    template_name = 'announcements/moderate.html'
    context_object_name = 'announcements'
    permission_required = 'webapp.can_moderated'

    def get_queryset(self):
        return super().get_queryset().exclude(status='published')


class StatusView(View):

    def get(self, request, *args, **kwargs):
        a = get_object_or_404(Announcement, pk=self.kwargs.get('pk'))
        if a.status == 'published':
            a.save()
        else:
            a.remove()
        response = JsonResponse({})
        return response



