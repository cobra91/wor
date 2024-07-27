from django import forms
from .models import Weapon, Chestplate, Wristband, Amulet, Ring


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            "main_stat_value",
            "first_stat",
            "first_stat_value",
            "second_stat",
            "second_stat_value",
            "third_stat",
            "third_stat_value",
            "fourth_stat",
            "fourth_stat_value",
            "set_name",
        ]


class ChestplateForm(forms.ModelForm):
    class Meta:
        model = Chestplate
        fields = [
            "main_stat_value",
            "first_stat",
            "first_stat_value",
            "second_stat",
            "second_stat_value",
            "third_stat",
            "third_stat_value",
            "fourth_stat",
            "fourth_stat_value",
            "set_name",
        ]


class WristbandForm(forms.ModelForm):
    class Meta:
        model = Wristband
        fields = [
            "main_stat",
            "main_stat_value",
            "first_stat",
            "first_stat_value",
            "second_stat",
            "second_stat_value",
            "third_stat",
            "third_stat_value",
            "fourth_stat",
            "fourth_stat_value",
            "set_name",
        ]


class AmuletForm(forms.ModelForm):
    class Meta:
        model = Amulet
        fields = [
            "main_stat",
            "main_stat_value",
            "first_stat",
            "first_stat_value",
            "second_stat",
            "second_stat_value",
            "third_stat",
            "third_stat_value",
            "fourth_stat",
            "fourth_stat_value",
            "set_name",
        ]


class RingForm(forms.ModelForm):
    class Meta:
        model = Ring
        fields = [
            "main_stat",
            "main_stat_value",
            "first_stat",
            "first_stat_value",
            "second_stat",
            "second_stat_value",
            "third_stat",
            "third_stat_value",
            "fourth_stat",
            "fourth_stat_value",
            "set_name",
        ]
