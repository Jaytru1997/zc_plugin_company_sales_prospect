from django.urls import path
from prospect.views import (
    GetPropects,
    ProspectsBatchDeleteView,
    ProspectsCreateView,
    ProspectsDeleteView,
    ProspectsListView,
    ProspectsUpdateView,
    WelcomeView,
    search_prospects,
)

urlpatterns = [
    path("search/<str:search>/", search_prospects, name="search"),
    # path("search/<str:search>/", SearchProspects, name="search"),
    path("<str:org_id>/<str:user_id>/create/", ProspectsCreateView.as_view()),
    path("<str:org_id>/", ProspectsListView.as_view(), name="prospects"),
    path("", GetPropects.as_view(), name="prospects"),
    path("welcome/", WelcomeView.as_view(), name="welcome_mail"),
    path("<str:org_id>/update/", ProspectsUpdateView.as_view()),
    path("delete/batch/", ProspectsBatchDeleteView.as_view()),
    path("delete/<str:search>/", ProspectsDeleteView.as_view()),
    # path("details/<str:id>/", ProspectDetailsView.as_view()),
]

# reminder to remove the org_id
