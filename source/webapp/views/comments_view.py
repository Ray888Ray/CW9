from django.shortcuts import reverse, get_object_or_404
from webapp.forms import CommentForm
from webapp.models import Comment, Announcement
from django.views.generic import CreateView, DeleteView


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'comments/create_comment.html'
    model = Comment

    def form_valid(self, form):
        announcements = get_object_or_404(Announcement, pk=self.kwargs.get('pk'))
        user = self.request.user
        form.instance.announcements = announcements
        form.instance.comments_author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:info', kwargs={'pk': self.object.announcements.pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:info', kwargs={'pk': self.object.announcements.pk})
