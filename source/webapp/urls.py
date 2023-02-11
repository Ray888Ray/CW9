from webapp.views.announcements_views import AnnouncementIndexView, AnnouncementView, AnnouncementCreateView, \
    AnnouncementUpdateView, AnnouncementDeletesView, ListModeratedView, StatusView
from webapp.views.comments_view import CommentCreateView, CommentDeleteView
from django.urls import path

app_name = 'webapp'


urlpatterns = [
    path('', AnnouncementIndexView.as_view(), name='index'),
    path('<int:pk>/', AnnouncementView.as_view(), name='info'),
    path('create/', AnnouncementCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AnnouncementUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AnnouncementDeletesView.as_view(), name='delete'),
    path('moderate/', ListModeratedView.as_view(), name='moderate'),
    path('accept/<int:pk>/', StatusView.as_view(), name='status'),


    path('comment/create/<int:pk>', CommentCreateView.as_view(), name='comments_create'),
    path('comment/delete/<int:pk>', CommentDeleteView.as_view(), name='comments_delete'),
]