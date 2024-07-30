from django.urls import path

from . import views

app_name = "wor"
urlpatterns = [
    path("", views.index_show_view, name="index"),
    path("compareEquipmentForm/", views.compare_equipment_form_view, name="compare_equipment_url"),
    path("characterShow/", views.CharacterView.as_view(), name="show_character_url"),
    path("character/<int:pk>/", views.CharacterDetailView.as_view(), name="character-detail"),
    path("characterForm/", views.character_form_view, name="character_url"),
    path("weaponForm/", views.weapon_form_view, name="weapon_url"),
    path("chestplateForm/", views.chestplate_form_view, name="chestplate_url"),
    path("wristbandForm/", views.wristband_form_view, name="wristband_url"),
    path("amuletForm/", views.amulet_form_view, name="amulet_url"),
    path("ringForm/", views.ring_form_view, name="ring_url"),
    path("weaponShow/", views.weapon_show_view, name="show_weapon_url"),
    path("chestplateShow/", views.chestplate_show_view, name="show_chestplate_url"),
    path("wristbandShow/", views.wristband_show_view, name="show_wristband_url"),
    path("amuletShow/", views.amulet_show_view, name="show_amulet_url"),
    path("ringShow/", views.ring_show_view, name="show_ring_url"),
    path("character/<int:f_id>/change", views.character_update_view, name="update_character_url"),
    path("weapon/<int:f_id>/change", views.weapon_update_view, name="update_weapon_url"),
    path("chestplate/<int:f_id>/change", views.chestplate_update_view, name="update_chestplate_url"),
    path("wristband/<int:f_id>/change", views.wristband_update_view, name="update_wristband_url"),
    path("amulet/<int:f_id>/change", views.amulet_update_view, name="update_amulet_url"),
    path("ring/<int:f_id>/change", views.ring_update_view, name="update_ring_url"),
    path("weapon/<int:f_id>/delete", views.weapon_delete_view, name="delete_weapon_url"),
    path("chestplate/<int:f_id>/delete", views.chestplate_delete_view, name="delete_chestplate_url"),
    path("wristband/<int:f_id>/delete", views.wristband_delete_view, name="delete_wristband_url"),
    path("amulet/<int:f_id>/delete", views.amulet_delete_view, name="delete_amulet_url"),
    path("ring/<int:f_id>/delete", views.ring_delete_view, name="delete_ring_url"),
    path("weapon/<int:id>", views.weapon_detail, name="weapon-detail"),
    path("chestplate/<int:id>/", views.chestplate_detail, name="chestplate-detail"),
    path("wristband/<int:id>/", views.wristband_detail, name="wristband-detail"),
    path("amulet/<int:id>/", views.amulet_detail, name="amulet-detail"),
    path("ring/<int:id>/", views.ring_detail, name="ring-detail"),
]
