import copy

from django import forms

from .models import Amulet, Character, Chestplate, Ring, Weapon, Wristband, Pantheon, Artifact, Collection


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
    if (
        good_hp_value
        and good_atk_value
        and good_def_value
        and good_crit_rate_value
        and good_crit_dmg_value
        and good_vit_interval_value
        and good_rage_regen_value
        and good_heal_effect_value
    ):
        return True
    else:
        return False


class CompareEquipmentForm(forms.Form):
    character: Character = forms.ModelChoiceField(queryset=Character.objects.all().order_by("name"))
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
    defense_reduction = forms.IntegerField(required=False, min_value=0, initial=0)
    use_equipped_items = forms.BooleanField(required=False)
    skill_buff = forms.ChoiceField(
        required=False,
        choices=(
            ("", "None"),
            ("Laurel", "Symbiotic Power (Laurel)"),
            ("Dolores", "Graceful Dancing (Dolores)"),
            ("Autumn", "Gold Maple's Room (Autumn)"),
        ),
    )
    dolo_skill_buff = forms.IntegerField(
        required=False,
        min_value=0,
        initial=0,
        widget=forms.TextInput(attrs={'placeholder': 'Dolores Total Attack', 'type': "number"}),
    )
    resultlist: list[list[object]] = []
    characterEquipList: list[Character] = []

    def compare(self) -> list[list[object]]:
        self.resultlist.clear()
        self.characterEquipList.clear()
        character: Character = self.cleaned_data["character"]
        weapon_equiped = Weapon.objects.all().filter(character_id__isnull=False)
        chestplate_equiped = Chestplate.objects.all().filter(character_id__isnull=False)
        wristband_equiped = Wristband.objects.all().filter(character_id__isnull=False)
        amulet_equiped = Amulet.objects.all().filter(character_id__isnull=False)
        ring_equiped = Ring.objects.all().filter(character_id__isnull=False)
        for weapon in Weapon.objects.all().exclude(
            id__in='' if self.cleaned_data['use_equipped_items'] else weapon_equiped
        ):
            for chestplate in Chestplate.objects.all().exclude(
                id__in='' if self.cleaned_data['use_equipped_items'] else chestplate_equiped
            ):
                for wristband in Wristband.objects.all().exclude(
                    id__in='' if self.cleaned_data['use_equipped_items'] else wristband_equiped
                ):
                    for amulet in Amulet.objects.all().exclude(
                        id__in='' if self.cleaned_data['use_equipped_items'] else amulet_equiped
                    ):
                        for ring in Ring.objects.all().exclude(
                            id__in='' if self.cleaned_data['use_equipped_items'] else ring_equiped
                        ):
                            crt_equipment: list[object] = []
                            crt_character: Character = copy.deepcopy(character)
                            crt_character.weapon = weapon
                            crt_character.chestplate = chestplate
                            crt_character.wristband = wristband
                            crt_character.amulet = amulet
                            crt_character.ring = ring
                            crt_character._defence_reduction = self.cleaned_data['defense_reduction']
                            crt_character._skill_buff = self.cleaned_data['skill_buff']
                            crt_character._dolo_skill_buff = self.cleaned_data['dolo_skill_buff']
                            crt_character._user_id = self.data['user_id'] if self.data['user_id'] != '' else 0
                            if equipment_goodvalue(self, crt_character):
                                crt_equipment.append(weapon)
                                crt_equipment.append(chestplate)
                                crt_equipment.append(wristband)
                                crt_equipment.append(amulet)
                                crt_equipment.append(ring)
                                self.characterEquipList.append(crt_character)
                                self.resultlist.append(crt_equipment)
        return self.resultlist


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "rarity",
            "heroclass",
            "faction",
            "damagetype",
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
            "rage_regen",
            "rage_regen_auto",
            "rage_regen_basic_atk",
            "rage_regen_atked",
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
            "character",
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
            "character",
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
            "character",
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
            "character",
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
            "character",
        ]


class PantheonForm(forms.ModelForm):
    class Meta:
        model = Pantheon
        fields = [
            "atk_bonus",
            "hp_bonus",
            "rage_regen",
            "crit_dmg",
            "healing_effect",
            "atk_spd",
            "def_bonus",
            "mRes_bonus",
            "crit_rate",
            "ragen_regen_auto",
        ]


class ArtifactForm(forms.ModelForm):
    class Meta:
        model = Artifact
        fields = [
            "hp",
            "atk",
            "character",
        ]


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "hp50",
            "hp200_watcher",
            "hp200_north",
            "hp200_curse",
            "hp200_nightmare",
            "hp200_infernal",
            "hp200_piercer",
            "hp200_esoteric",
            "hp200_chaos_dominion",
            "hp200_arbiters",
            "hp400",
            "rage_regen_atked",
            "atk50_north",
            "atk50_curse",
            "atk50_nightmare",
            "atk50_infernal",
            "atk50_piercer",
            "atk50_esoteric",
            "atk50_chaos_dominion",
            "atk50_arbiters",
            "revival_time_minus_5",
            "rage_regen_basic_atk_1_nightmare",
            "rage_regen_basic_atk_1_piercer",
            "crit_rate_3",
            "crit_dmg_5",
            "init_rage_30",
        ]


class WatcherCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "hp50",
            "hp200_watcher",
            "rage_regen_atked",
        ]


class NorthCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_north",
            "hp200_north",
            "revival_time_minus_5",
        ]


class NightmareCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_nightmare",
            "hp200_nightmare",
            "rage_regen_basic_atk_1_nightmare",
        ]


class CurseCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_curse",
            "hp200_curse",
            "crit_rate_3",
        ]


class InfernalCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_infernal",
            "hp200_infernal",
            "crit_dmg_5",
        ]


class PiercerCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_piercer",
            "hp200_piercer",
            "rage_regen_basic_atk_1_piercer",
        ]


class EsotericCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_esoteric",
            "hp200_esoteric",
            "init_rage_30",
        ]


class ChaosDominionCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_chaos_dominion",
            "hp200_chaos_dominion",
            "hp400",
        ]


class ArbitersCollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = [
            "faction",
            "atk50_arbiters",
            "hp200_arbiters",
        ]
