from django.contrib import admin

from .models import Amulet, Character, Chestplate, Faction, HeroClass, Rarity, Ring, Weapon, Wristband


class AttributeAdmin2P(admin.ModelAdmin):
    fields = (
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
    )
    list_display = [
        "id",
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
        "set_bonus",
    ]


class AttributeAdmin3P(admin.ModelAdmin):
    fields = (
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
    )
    list_display = [
        "id",
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
        "set_bonus",
    ]


class WeaponAdmin(AttributeAdmin2P):
    pass


class ChestplateAdmin(AttributeAdmin2P):
    pass


class WristbandAdmin(AttributeAdmin3P):
    pass


class AmuletAdmin(AttributeAdmin3P):
    pass


class RingAdmin(AttributeAdmin3P):
    pass


admin.site.register(Rarity)
admin.site.register(HeroClass)
admin.site.register(Faction)
admin.site.register(Character)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(Chestplate, ChestplateAdmin)
admin.site.register(Wristband, WristbandAdmin)
admin.site.register(Amulet, AmuletAdmin)
admin.site.register(Ring, RingAdmin)
