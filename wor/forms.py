import copy

from django import forms

from .models import Amulet, Character, Chestplate, Ring, Weapon, Wristband


def equipment_goodvalue(self, crt_character: Character) -> bool:
    good_hp_value = False
    good_atk_value = False
    good_def_value = False
    good_crit_rate_value = False
    good_crit_dmg_value = False
    good_vit_interval_value = False
    good_rage_regen_value = False
    good_heal_effect_value = False
    if self.cleaned_data['hp_min'] or self.cleaned_data['hp_max']:
        if (
            (self.cleaned_data['hp_min'] if self.cleaned_data['hp_min'] else 0)
            < crt_character.total_hp
            < (self.cleaned_data['hp_max'] if self.cleaned_data['hp_max'] else 999999)
        ):
            good_hp_value = True
    else:
        good_hp_value = True
    if self.cleaned_data['atk_min'] or self.cleaned_data['atk_max']:
        if (
            (self.cleaned_data['atk_min'] if self.cleaned_data['atk_min'] else 0)
            < crt_character.total_atk
            < (self.cleaned_data['atk_max'] if self.cleaned_data['atk_max'] else 999999)
        ):
            good_atk_value = True
    else:
        good_atk_value = True
    if self.cleaned_data['def_min'] or self.cleaned_data['def_max']:
        if (
            (self.cleaned_data['def_min'] if self.cleaned_data['def_min'] else 0)
            < crt_character.total_def
            < (self.cleaned_data['def_max'] if self.cleaned_data['def_max'] else 999999)
        ):
            good_def_value = True
    else:
        good_def_value = True
    if self.cleaned_data['crit_rate_min'] or self.cleaned_data['crit_rate_max']:
        if (
            (self.cleaned_data['crit_rate_min'] if self.cleaned_data['crit_rate_min'] else 0)
            < crt_character.total_crit_rate
            < (self.cleaned_data['crit_rate_max'] if self.cleaned_data['crit_rate_max'] else 999999)
        ):
            good_crit_rate_value = True
    else:
        good_crit_rate_value = True
    if self.cleaned_data['crit_dmg_min'] or self.cleaned_data['crit_dmg_max']:
        if (
            (self.cleaned_data['crit_dmg_min'] if self.cleaned_data['crit_dmg_min'] else 0)
            < crt_character.total_crit_dmg
            < (self.cleaned_data['crit_dmg_max'] if self.cleaned_data['crit_dmg_max'] else 999999)
        ):
            good_crit_dmg_value = True
    else:
        good_crit_dmg_value = True
    if self.cleaned_data['vit_interval_min'] or self.cleaned_data['vit_interval_max']:
        if (
            (self.cleaned_data['vit_interval_min'] if self.cleaned_data['vit_interval_min'] else 0)
            < crt_character.total_attack_interval
            < (self.cleaned_data['vit_interval_max'] if self.cleaned_data['vit_interval_max'] else 999999)
        ):
            good_vit_interval_value = True
    else:
        good_vit_interval_value = True
    if self.cleaned_data['rage_regen_min'] or self.cleaned_data['rage_regen_max']:
        if (
            (self.cleaned_data['rage_regen_min'] if self.cleaned_data['rage_regen_min'] else 0)
            < crt_character.total_rage_regen
            < (self.cleaned_data['rage_regen_max'] if self.cleaned_data['rage_regen_max'] else 999999)
        ):
            good_rage_regen_value = True
    else:
        good_rage_regen_value = True
    if self.cleaned_data['heal_effect_min'] or self.cleaned_data['heal_effect_max']:
        if (
            (self.cleaned_data['heal_effect_min'] if self.cleaned_data['heal_effect_min'] else 0)
            < crt_character.total_heal_effect
            < (self.cleaned_data['heal_effect_max'] if self.cleaned_data['heal_effect_max'] else 999999)
        ):
            good_heal_effect_value = True
    else:
        good_heal_effect_value = True
    return (
        good_hp_value
        and good_atk_value
        and good_def_value
        and good_crit_rate_value
        and good_crit_dmg_value
        and good_vit_interval_value
        and good_rage_regen_value
        and good_heal_effect_value
    )


class CompareEquipmentForm(forms.Form):
    character: Character = forms.ModelChoiceField(queryset=Character.objects.all())
    hp_min = forms.IntegerField(required=False, min_value=0)
    hp_max = forms.IntegerField(required=False, min_value=0)
    atk_min = forms.IntegerField(required=False, min_value=0)
    atk_max = forms.IntegerField(required=False, min_value=0)
    def_min = forms.IntegerField(required=False, min_value=0)
    def_max = forms.IntegerField(required=False, min_value=0)
    crit_rate_min = forms.IntegerField(required=False, min_value=0)
    crit_rate_max = forms.IntegerField(required=False, min_value=0)
    crit_dmg_min = forms.IntegerField(required=False, min_value=0)
    crit_dmg_max = forms.IntegerField(required=False, min_value=0)
    vit_interval_min = forms.FloatField(required=False, min_value=0)
    vit_interval_max = forms.FloatField(required=False, min_value=0)
    rage_regen_min = forms.IntegerField(required=False, min_value=0)
    rage_regen_max = forms.IntegerField(required=False, min_value=0)
    heal_effect_min = forms.IntegerField(required=False, min_value=0)
    heal_effect_max = forms.IntegerField(required=False, min_value=0)
    resultlist: list[list[object]] = []
    characterEquipList: list[Character] = []

    def compare(self) -> list[list[object]]:
        self.resultlist.clear()
        self.characterEquipList.clear()
        character: Character = self.cleaned_data["character"]
        for weapon in Weapon.objects.all():
            for chestplate in Chestplate.objects.all():
                for wristband in Wristband.objects.all():
                    for amulet in Amulet.objects.all():
                        for ring in Ring.objects.all():
                            crt_equipment: list[object] = []
                            crt_character = copy.deepcopy(character)
                            crt_character.weapon = weapon
                            crt_character.chestplate = chestplate
                            crt_character.wrisband = wristband
                            crt_character.amulet = amulet
                            crt_character.ring = ring
                            if equipment_goodvalue(self, crt_character):
                                crt_equipment.append(weapon)
                                crt_equipment.append(chestplate)
                                crt_equipment.append(wristband)
                                crt_equipment.append(amulet)
                                crt_equipment.append(ring)
                                self.characterEquipList.append(crt_character)
                                self.resultlist.append(crt_equipment)

        # for chestplate in Chestplate.objects.all():
        #     if equipment_goodvalue(self, chestplate):
        #         self.resultlist.append(chestplate)
        #         crt_character = self.cleaned_data["character"]
        #         crt_character.chestplate = chestplate
        #         self.characterEquipList.append(crt_character)
        # for wristband in Wristband.objects.all():
        #     if equipment_goodvalue(self, wristband):
        #         self.resultlist.append(wristband)
        #         crt_character = self.cleaned_data["character"]
        #         crt_character.wristband = wristband
        #         self.characterEquipList.append(crt_character)
        # for amulet in Amulet.objects.all():
        #     if equipment_goodvalue(self, amulet):
        #         self.resultlist.append(amulet)
        #         crt_character = self.cleaned_data["character"]
        #         crt_character.amulet = amulet
        #         self.characterEquipList.append(crt_character)
        # for ring in Ring.objects.all():
        #     if equipment_goodvalue(self, ring):
        #         self.resultlist.append(ring)
        #         crt_character = self.cleaned_data["character"]
        #         crt_character.ring = ring
        #         self.characterEquipList.append(crt_character)

        return self.resultlist


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "rarity",
            "heroclass",
            "faction",
            "name",
            "health",
            "attack",
            "defense",
            "mRes",
            "cost",
            "block",
            "revival_time",
            "attack_interval",
            "crit_dmg",
            "attack_speed",
            "rage_regen_auto",
            "weapon",
            "chestplate",
            "wrisband",
            "amulet",
            "ring",
        ]


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
