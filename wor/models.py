from decimal import ROUND_HALF_UP, Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ManyToManyField
from django.utils.translation import gettext_lazy as _

from wor.constant import crit_rate, rage_regen, vit_atq


class Rarity(models.Model):
    class RarityEnum(models.TextChoices):
        RARE = "Rare", _("Rare")
        EPIC = "Epic", _("Epic")
        LEGENDARY = "Legendary", _("Legendary")

    rarity = models.CharField(default=RarityEnum.RARE, choices=RarityEnum, max_length=10)

    def __str__(self):
        return self.rarity


class HeroClass(models.Model):
    class HeroClassEnum(models.TextChoices):
        FIGHTER = "Fighter", _("Fighter")
        MAGE = "Mage", _("Mage")
        MARKSMAN = "Marksman", _("Marksman")
        HEALER = "Healer", _("Healer")
        DEFENDER = "Defender", _("Defender")

    heroclass = models.CharField(default=HeroClassEnum.FIGHTER, choices=HeroClassEnum, max_length=10)

    def __str__(self):
        return self.heroclass


class Faction(models.Model):
    class FactionEnum(models.TextChoices):
        WATCHER = "Watcher", _("Watcher")
        NORTH = "North", _("North")
        NIGHTMARE = "Nightmare", _("Nightmare")
        CURSE = "Curse", _("Curse")
        INFERNAL = "Infernal", _("Infernal")
        PIERCER = "Piercer", _("Piercer")
        ESOTERIC = "Esoteric", _("Esoteric")
        CHAOS_DOMINION = "Chaos Dominion", _("Chaos Dominion")
        ARBITERS = "Arbiters", _("Arbiters")
        UNNAMABLE = "Unnamable", _("Unnamable")

    faction = models.CharField(default=FactionEnum.WATCHER, choices=FactionEnum, max_length=15)

    def __str__(self):
        return self.faction


class DamageType(models.Model):
    class DamageTypeEnum(models.TextChoices):
        PIERCING = "Piercing", _("Piercing")
        MAGIC = "Magic", _("Magic")
        NORMAL = "Normal", _("Normal")

    dmg_type = models.CharField(default=DamageTypeEnum.NORMAL, choices=DamageTypeEnum, max_length=8)

    def __str__(self):
        return self.dmg_type


class Attribute(models.Model):
    class AttributeEnum(models.TextChoices):
        ATQ = "atq", _("Atq")
        DEF = "def", _("Def")
        PV = "pv", _("Pv")
        ATQ_BONUS = "atq bonus", _("Atq bonus")
        DEF_BONUS = "def bonus", _("def bonus")
        PV_BONUS = "pv bonus", _("pv bonus")
        RAGE_REGEN = rage_regen, _(rage_regen)
        CRIT_RATE = crit_rate, _(crit_rate)
        CRIT_DMG = "crit dmg", _("crit dmg")
        HEAL_EFFECT = "heal effect", _("heal effect")
        VIT_ATQ = vit_atq, _(vit_atq)

    name = models.CharField(default=AttributeEnum.ATQ, choices=AttributeEnum, max_length=15)

    class Meta:
        abstract = True


class Equipment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")
    main_stat = models.CharField(
        choices=Attribute.AttributeEnum,
        max_length=15,
        default=Attribute.AttributeEnum.ATQ,
    )
    main_stat_value = models.FloatField(null=True, blank=True)
    first_stat = models.CharField(
        choices=Attribute.AttributeEnum,
        max_length=15,
        default=Attribute.AttributeEnum.ATQ,
    )
    first_stat_value = models.FloatField(null=True, blank=True)
    second_stat = models.CharField(
        choices=Attribute.AttributeEnum,
        max_length=15,
        default=Attribute.AttributeEnum.ATQ,
    )
    second_stat_value = models.FloatField(null=True, blank=True)
    third_stat = models.CharField(
        choices=Attribute.AttributeEnum,
        max_length=15,
        default=Attribute.AttributeEnum.ATQ,
    )
    third_stat_value = models.FloatField(null=True, blank=True)
    fourth_stat = models.CharField(
        choices=Attribute.AttributeEnum,
        max_length=15,
        default=Attribute.AttributeEnum.ATQ,
    )
    fourth_stat_value = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.OneToOneField("Character", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return " ".join(
            [
                self.main_stat,
                str(self.main_stat_value),
                self.first_stat,
                str(self.first_stat_value),
                self.second_stat,
                str(self.second_stat_value),
                self.third_stat,
                str(self.third_stat_value),
                self.fourth_stat,
                str(self.fourth_stat_value),
            ]
        )

    class Meta:
        abstract = True


class Set2pEnum(models.TextChoices):
    LIGHT_GRACE = "light's grace", _("Light's Grace")
    WICKED_VENGEANCE = "wicked vengeance", _("Wicker Vengeance")
    IMMORTAL_WARRIOR = "immortal warrior", _("Immortal Warrior")
    WARLORD = "warlord", _("Warlord")
    SALVATION = "salvation", _("Salvation")
    LIFE_FORCE = "life force", _("Life Force")
    CALAMITY = "calamity", _("Calamity")
    WHIRLWIND = "whirlwind", _("Whirlwind")
    ANNIHILATING_MIGHT = "annihilating might", _("Annihilating Might")
    LIFEGIVER = "lifegiver", _("Lifegiver")
    IRON_FORTRESS = "iron fortress", _("Iron Fortress")
    WRATHFUL_ONSLAUGHT = "wrathful onslaught", _("Wrathful Onslaught")
    SAVAGE_STRIKE = "savage strike", _("Savage Strike")
    DEADLY_AIM = "deadly aim", _("Deadly Aim")
    VITALITY = "vitality", _("Vitality")
    JUGGERNAUT = "juggernaut", _("Juggernaut")


def get_bonus_2p(set_name):
    match set_name:
        case Set2pEnum.JUGGERNAUT:
            return ""
        case Set2pEnum.VITALITY:
            return ""
        case Set2pEnum.DEADLY_AIM:
            return "Crit. Rate +10%"
        case Set2pEnum.SAVAGE_STRIKE:
            return ""
        case Set2pEnum.WRATHFUL_ONSLAUGHT:
            return ""
        case Set2pEnum.IRON_FORTRESS:
            return ""
        case Set2pEnum.LIFEGIVER:
            return ""
        case Set2pEnum.ANNIHILATING_MIGHT:
            return "+35 crit dmg"
        case Set2pEnum.WHIRLWIND:
            return "ATK Spd. +75"
        case Set2pEnum.CALAMITY:
            return "ATK +25%"
        case Set2pEnum.LIFE_FORCE:
            return "HP +25%"
        case Set2pEnum.SALVATION:
            return "Healing Effect +25"
        case Set2pEnum.WARLORD:
            return "ATK +25%, ATK Spd. +30"
        case Set2pEnum.IMMORTAL_WARRIOR:
            return "HP +25%, DEF +10% "
        case Set2pEnum.WICKED_VENGEANCE:
            return ""
        case Set2pEnum.LIGHT_GRACE:
            return "Healing Effect +30, Rage Regen +10%"
        case _:
            return None


class Set2p(models.Model):
    set_name = models.CharField(default=Set2pEnum.CALAMITY, choices=Set2pEnum, max_length=18)

    @property
    def set_bonus(self):
        set_bonus = get_bonus_2p(self.set_name)
        if set_bonus is None:
            return 0
        else:
            return set_bonus

    @set_bonus.setter
    def set_bonus(self, value):
        self.set_bonus = value

    class Meta:
        abstract = True


def get_bonus_3p(set_name):
    match set_name:
        case Set3p.Set3pEnum.THE_TEMPEST:
            return ""
        case Set3p.Set3pEnum.RAPIDITY:
            return "Cost -1"
        case Set3p.Set3pEnum.TWISTED_BLADE:
            return "DMG +10%"
        case Set3p.Set3pEnum.OCCULT_SHIELD:
            return "dmg taken -10%"
        case Set3p.Set3pEnum.GUARDIAN:
            return "dmg taken -15%"
        case Set3p.Set3pEnum.FATALITY:
            return "Increases ATK by 3% and ignores 12% of target's DEF and M.RES"
        case Set3p.Set3pEnum.CURSE:
            return "Increases DMG by 6% for up to 5 stacks for every ennemy within the ATK Range."
        case Set3p.Set3pEnum.FRACTURE:
            return "Increases Crit. DMG by 45% when HP is above 70%"
        case Set3p.Set3pEnum.MANA_SPRING:
            return "Rage regen (Auto) +3"
        case Set3p.Set3pEnum.HAWK_EYE:
            return "Launching 5 Basic ATK increased DMG by 25% for 6 sec."
        case Set3p.Set3pEnum.THE_GLACIER:
            return "Gain an ATK bonus equal to 6% Max HP when deployed."
        case Set3p.Set3pEnum.NIGHT_TERROR:
            return "Increases DMG by 25% for 3 sec after making Crit. Hits."
        case Set3p.Set3pEnum.THE_STYX:
            return "AoE DMG +18%"
        case Set3p.Set3pEnum.THE_DOOM:
            return "Single-Target DMG +18%"
        case Set3p.Set3pEnum.THE_WISDOM:
            return "After using Ultimate skills, increases DMG by 35% for 10 sec."
        case Set3p.Set3pEnum.THE_INSIGHT:
            return (
                "Crit. Rate +15%. Each single-target DMG dealt by Basic ATKs will deal extra DMG equal to 10 times "
                "the caster's level"
            )
        case Set3p.Set3pEnum.ASCLEPIUS:
            return "MAX HP +10%, Healing Effect +20"
        case Set3p.Set3pEnum.AGELESS_WRATH:
            return ""
        case Set3p.Set3pEnum.TEMPERED_WILL:
            return ""
        case Set3p.Set3pEnum.HELLS_LAMENT:
            return ""
        case Set3p.Set3pEnum.UNSHAKEN_WILL:
            return ""
        case Set3p.Set3pEnum.MORALE:
            return ""
        case Set3p.Set3pEnum.INFERNAL_ROAR:
            return "Basic ATK DMG +40%"
        case Set3p.Set3pEnum.SOULBOUND_ARCANA:
            return ""
        case Set3p.Set3pEnum.INVIGORATION:
            return ""
        case _:
            return None


class Set3p(models.Model):
    class Set3pEnum(models.TextChoices):
        TEMPERED_WILL = "tempered will", _("Tempered Will")
        HELLS_LAMENT = "hell's lament", _("Hell's Lament")
        UNSHAKEN_WILL = "unshaken will", _("Unshaken Will")
        MORALE = "morale", _("Morale")
        INFERNAL_ROAR = "infernal roar", _("Infernal Roar")
        SOULBOUND_ARCANA = "soulbound arcana", _("Soulbound Arcana")
        INVIGORATION = "invigoration", _("Invigoration")
        AGELESS_WRATH = "ageless wrath", _("Ageless Wrath")
        ASCLEPIUS = "asclepius", _("Asclepius")
        THE_INSIGHT = "the insight", _("The Insight")
        THE_WISDOM = "the wisdom", _("The Wisdom")
        THE_DOOM = "the doom", _("The Doom")
        THE_STYX = "the styx", _("The Styx")
        NIGHT_TERROR = "night terror", _("Night Terror")
        THE_GLACIER = "the glacier", _("The Glacier")
        HAWK_EYE = "hawk eye", _("Hawk Eye")
        MANA_SPRING = "mana spring", _("Mana Spring")
        FRACTURE = "fracture", _("Fracture")
        CURSE = "curse", _("Curse")
        FATALITY = "fatality", _("Fatality")
        GUARDIAN = "guardian", _("Guardian")
        OCCULT_SHIELD = "occult shield", _("Occult Shield")
        TWISTED_BLADE = "twisted blade", _("Twisted Blade")
        RAPIDITY = "rapidity", _("Rapidity")
        THE_TEMPEST = "the tempest", _("The Tempest")

    set_name = models.CharField(default=Set3pEnum.THE_TEMPEST, choices=Set3pEnum, max_length=18)

    @property
    def set_bonus(self):
        set_bonus = get_bonus_3p(self.set_name)
        if set_bonus is None:
            return 0
        else:
            return set_bonus

    @set_bonus.setter
    def set_bonus(self, value):
        self.set_bonus = value

    class Meta:
        abstract = True


class Weapon(Equipment, Set2p):
    main_stat = models.CharField(max_length=16, default=Attribute.AttributeEnum.ATQ, editable=False)

    @property
    def get_model_type(self):
        return "Weapon"


class Chestplate(Equipment, Set2p):
    main_stat = models.CharField(max_length=16, default=Attribute.AttributeEnum.PV, editable=False)

    @property
    def get_model_type(self):
        return "Chestplate"


class Wristband(Equipment, Set3p):
    override_choice = list(
        filter(
            lambda x: x[1] != rage_regen and x[1] != vit_atq,
            Attribute.AttributeEnum.choices,
        )
    )
    main_stat = models.CharField(
        choices=override_choice,
        max_length=16,
        default=Attribute.AttributeEnum.ATQ,
    )

    @property
    def get_model_type(self):
        return "Wristband"


class Amulet(Equipment, Set3p):
    override_choice = list(
        filter(
            lambda x: x[1] != crit_rate and x[1] != rage_regen,
            Attribute.AttributeEnum.choices,
        )
    )
    main_stat = models.CharField(
        choices=override_choice,
        max_length=16,
        default=Attribute.AttributeEnum.ATQ,
    )

    @property
    def get_model_type(self):
        return "Amulet"


class Ring(Equipment, Set3p):
    override_choice = list(
        filter(
            lambda x: x[1] != crit_rate and x[1] != vit_atq,
            Attribute.AttributeEnum.choices,
        )
    )
    main_stat = models.CharField(
        choices=override_choice,
        max_length=16,
        default=Attribute.AttributeEnum.ATQ,
    )

    @property
    def get_model_type(self):
        return "Ring"


def hp_equipment(basehealth: int, equipment: Weapon | Chestplate | Wristband | Amulet | Ring) -> int:
    total_hp: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat
        in (
            Attribute.AttributeEnum.PV,
            Attribute.AttributeEnum.PV_BONUS,
        )
    ):
        if equipment.main_stat == Attribute.AttributeEnum.PV:
            total_hp += equipment.main_stat_value
        else:
            total_hp += basehealth * equipment.main_stat_value / 100

    if hasattr(equipment, "first_stat") and equipment.first_stat in (
        Attribute.AttributeEnum.PV,
        Attribute.AttributeEnum.PV_BONUS,
    ):
        if equipment.first_stat == Attribute.AttributeEnum.PV:
            total_hp += equipment.first_stat_value
        else:
            total_hp += basehealth * equipment.first_stat_value / 100

    if hasattr(equipment, "second_stat") and equipment.second_stat in (
        Attribute.AttributeEnum.PV,
        Attribute.AttributeEnum.PV_BONUS,
    ):
        if equipment.second_stat == Attribute.AttributeEnum.PV:
            total_hp += equipment.second_stat_value
        else:
            total_hp += basehealth * equipment.second_stat_value / 100

    if hasattr(equipment, "third_stat") and equipment.third_stat in (
        Attribute.AttributeEnum.PV,
        Attribute.AttributeEnum.PV_BONUS,
    ):
        if equipment.third_stat == Attribute.AttributeEnum.PV:
            total_hp += equipment.third_stat_value
        else:
            total_hp += basehealth * equipment.third_stat_value / 100
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat in (
        Attribute.AttributeEnum.PV,
        Attribute.AttributeEnum.PV_BONUS,
    ):
        if equipment.fourth_stat == Attribute.AttributeEnum.PV:
            total_hp += equipment.fourth_stat_value
        else:
            total_hp += basehealth * equipment.fourth_stat_value / 100
    return int(total_hp)


def atk_equipment(baseattack: int, equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_atk: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat
        in (
            Attribute.AttributeEnum.ATQ,
            Attribute.AttributeEnum.ATQ_BONUS,
        )
    ):
        if equipment.main_stat == Attribute.AttributeEnum.ATQ:
            total_atk += equipment.main_stat_value
        else:
            total_atk += baseattack * equipment.main_stat_value / 100
    if hasattr(equipment, "first_stat") and equipment.first_stat in (
        Attribute.AttributeEnum.ATQ,
        Attribute.AttributeEnum.ATQ_BONUS,
    ):
        if equipment.first_stat == Attribute.AttributeEnum.ATQ:
            total_atk += equipment.first_stat_value
        else:
            total_atk += baseattack * equipment.first_stat_value / 100

    if hasattr(equipment, "second_stat") and equipment.second_stat in (
        Attribute.AttributeEnum.ATQ,
        Attribute.AttributeEnum.ATQ_BONUS,
    ):
        if equipment.second_stat == Attribute.AttributeEnum.ATQ:
            total_atk += equipment.second_stat_value
        else:
            total_atk += baseattack * equipment.second_stat_value / 100

    if hasattr(equipment, "third_stat") and equipment.third_stat in (
        Attribute.AttributeEnum.ATQ,
        Attribute.AttributeEnum.ATQ_BONUS,
    ):
        if equipment.third_stat == Attribute.AttributeEnum.ATQ:
            total_atk += equipment.third_stat_value
        else:
            total_atk += baseattack * equipment.third_stat_value / 100
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat in (
        Attribute.AttributeEnum.ATQ,
        Attribute.AttributeEnum.ATQ_BONUS,
    ):
        if equipment.fourth_stat == Attribute.AttributeEnum.ATQ:
            total_atk += equipment.fourth_stat_value
        else:
            total_atk += baseattack * equipment.fourth_stat_value / 100
    return total_atk


def def_equipment(basedef: int, equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_def: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat
        in (
            Attribute.AttributeEnum.DEF,
            Attribute.AttributeEnum.DEF_BONUS,
        )
    ):
        if equipment.main_stat == Attribute.AttributeEnum.DEF:
            total_def += equipment.main_stat_value
        else:
            total_def += basedef * equipment.main_stat_value / 100
    if hasattr(equipment, "first_stat") and equipment.first_stat in (
        Attribute.AttributeEnum.DEF,
        Attribute.AttributeEnum.DEF_BONUS,
    ):
        if equipment.first_stat == Attribute.AttributeEnum.DEF:
            total_def += equipment.first_stat_value
        else:
            total_def += basedef * equipment.first_stat_value / 100

    if hasattr(equipment, "second_stat") and equipment.second_stat in (
        Attribute.AttributeEnum.DEF,
        Attribute.AttributeEnum.DEF_BONUS,
    ):
        if equipment.second_stat == Attribute.AttributeEnum.DEF:
            total_def += equipment.second_stat_value
        else:
            total_def += basedef * equipment.second_stat_value / 100

    if hasattr(equipment, "third_stat") and equipment.third_stat in (
        Attribute.AttributeEnum.DEF,
        Attribute.AttributeEnum.DEF_BONUS,
    ):
        if equipment.third_stat == Attribute.AttributeEnum.DEF:
            total_def += equipment.third_stat_value
        else:
            total_def += basedef * equipment.third_stat_value / 100
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat in (
        Attribute.AttributeEnum.DEF,
        Attribute.AttributeEnum.DEF_BONUS,
    ):
        if equipment.fourth_stat == Attribute.AttributeEnum.DEF:
            total_def += equipment.fourth_stat_value
        else:
            total_def += basedef * equipment.fourth_stat_value / 100
    return total_def


def crit_rate_equipment(equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_crit_rate: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat == Attribute.AttributeEnum.CRIT_RATE
    ):
        total_crit_rate += equipment.main_stat_value
    if hasattr(equipment, "first_stat") and equipment.first_stat == Attribute.AttributeEnum.CRIT_RATE:
        total_crit_rate += equipment.first_stat_value
    if hasattr(equipment, "second_stat") and equipment.second_stat == Attribute.AttributeEnum.CRIT_RATE:
        total_crit_rate += equipment.second_stat_value
    if hasattr(equipment, "third_stat") and equipment.third_stat == Attribute.AttributeEnum.CRIT_RATE:
        total_crit_rate += equipment.third_stat_value
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat == Attribute.AttributeEnum.CRIT_RATE:
        total_crit_rate += equipment.fourth_stat_value
    return total_crit_rate


def crit_dmg_equipment(equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_crit_dmg: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat == Attribute.AttributeEnum.CRIT_DMG
    ):
        total_crit_dmg += equipment.main_stat_value
    if hasattr(equipment, "first_stat") and equipment.first_stat == Attribute.AttributeEnum.CRIT_DMG:
        total_crit_dmg += equipment.first_stat_value
    if hasattr(equipment, "second_stat") and equipment.second_stat == Attribute.AttributeEnum.CRIT_DMG:
        total_crit_dmg += equipment.second_stat_value
    if hasattr(equipment, "third_stat") and equipment.third_stat == Attribute.AttributeEnum.CRIT_DMG:
        total_crit_dmg += equipment.third_stat_value
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat == Attribute.AttributeEnum.CRIT_DMG:
        total_crit_dmg += equipment.fourth_stat_value
    return total_crit_dmg


def attack_speed_equipment(equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_attack_speed: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat == Attribute.AttributeEnum.VIT_ATQ
    ):
        total_attack_speed += equipment.main_stat_value
    if hasattr(equipment, "first_stat") and equipment.first_stat == Attribute.AttributeEnum.VIT_ATQ:
        total_attack_speed += equipment.first_stat_value
    if hasattr(equipment, "second_stat") and equipment.second_stat == Attribute.AttributeEnum.VIT_ATQ:
        total_attack_speed += equipment.second_stat_value
    if hasattr(equipment, "third_stat") and equipment.third_stat == Attribute.AttributeEnum.VIT_ATQ:
        total_attack_speed += equipment.third_stat_value
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat == Attribute.AttributeEnum.VIT_ATQ:
        total_attack_speed += equipment.fourth_stat_value
    return total_attack_speed


def rage_regen_equipment(equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_rage_regen: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat == Attribute.AttributeEnum.RAGE_REGEN
    ):
        total_rage_regen += equipment.main_stat_value
    if hasattr(equipment, "first_stat") and equipment.first_stat == Attribute.AttributeEnum.RAGE_REGEN:
        total_rage_regen += equipment.first_stat_value
    if hasattr(equipment, "second_stat") and equipment.second_stat == Attribute.AttributeEnum.RAGE_REGEN:
        total_rage_regen += equipment.second_stat_value
    if hasattr(equipment, "third_stat") and equipment.third_stat == Attribute.AttributeEnum.RAGE_REGEN:
        total_rage_regen += equipment.third_stat_value
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat == Attribute.AttributeEnum.RAGE_REGEN:
        total_rage_regen += equipment.fourth_stat_value
    return total_rage_regen


def healing_effect_equipment(equipment: Weapon | Chestplate | Wristband | Amulet | Ring):
    total_heal_effect: int = 0
    if (
        type(equipment) in (Wristband, Amulet, Ring)
        and hasattr(equipment, "main_stat")
        and equipment.main_stat == Attribute.AttributeEnum.HEAL_EFFECT
    ):
        total_heal_effect += equipment.main_stat_value
    if hasattr(equipment, "first_stat") and equipment.first_stat == Attribute.AttributeEnum.HEAL_EFFECT:
        total_heal_effect += equipment.first_stat_value
    if hasattr(equipment, "second_stat") and equipment.second_stat == Attribute.AttributeEnum.HEAL_EFFECT:
        total_heal_effect += equipment.second_stat_value
    if hasattr(equipment, "third_stat") and equipment.third_stat == Attribute.AttributeEnum.HEAL_EFFECT:
        total_heal_effect += equipment.third_stat_value
    if hasattr(equipment, "fourth_stat") and equipment.fourth_stat == Attribute.AttributeEnum.HEAL_EFFECT:
        total_heal_effect += equipment.fourth_stat_value
    return total_heal_effect


def attack_interval_equipment(attack_interval: float, attack_speed_gear: int) -> float:
    if attack_interval == 5.0:
        match attack_speed_gear:
            case num if num in range(41, 49):
                return 4.3
            case num if num in range(49, 58):
                return 4.2
            case num if num in range(58, 67):
                return 4.1
            case num if num in range(67, 77):
                return 4.0
            case num if num in range(77, 89):
                return 3.9
            case num if num in range(89, 101):
                return 3.8
            case num if num in range(101, 114):
                return 3.7
            case num if num in range(114, 128):
                return 3.6
            case num if num in range(128, 143):
                return 3.5
            case num if num in range(143, 161):
                return 3.4
            case num if num in range(161, 179):
                return 3.3
            case num if num in range(179, 201):
                return 3.2
            case num if num in range(201, 224):
                return 3.1
            case num if num in range(224, 251):
                return 3.0
            case num if num in range(251, 281):
                return 2.9
            case num if num in range(281, 315):
                return 2.8
            case num if num in range(315, 354):
                return 2.7
            case num if num in range(354, 401):
                return 2.6
            case num if num in range(401, 99999):
                return 2.5
    if attack_interval == 3.5:
        match attack_speed_gear:
            case num if num in range(38, 50):
                return 3.0
            case num if num in range(50, 63):
                return 2.9
            case num if num in range(63, 77):
                return 2.8
            case num if num in range(77, 94):
                return 2.7
            case num if num in range(94, 112):
                return 2.6
            case num if num in range(112, 132):
                return 2.5
            case num if num in range(132, 155):
                return 2.4
            case num if num in range(155, 182):
                return 2.3
            case num if num in range(182, 214):
                return 2.2
            case num if num in range(214, 251):
                return 2.1
            case num if num in range(251, 295):
                return 2.0
            case num if num in range(295, 348):
                return 1.9
            case num if num in range(348, 415):
                return 1.8
            case num if num in range(415, 99999):
                return 1.7
    if attack_interval == 3.0:
        match attack_speed_gear:
            case num if num in range(46, 61):
                return 2.5
            case num if num in range(61, 77):
                return 2.4
            case num if num in range(77, 96):
                return 2.3
            case num if num in range(96, 118):
                return 2.2
            case num if num in range(118, 143):
                return 2.1
            case num if num in range(143, 173):
                return 2.0
            case num if num in range(173, 208):
                return 1.9
            case num if num in range(208, 251):
                return 1.8
            case num if num in range(251, 303):
                return 1.7
            case num if num in range(303, 369):
                return 1.6
            case num if num in range(369, 9999):
                return 1.5
    if attack_interval == 2.6:
        match attack_speed_gear:
            case num if num in range(39, 55):
                return 2.2
            case num if num in range(55, 73):
                return 2.1
            case num if num in range(73, 95):
                return 2.0
            case num if num in range(95, 120):
                return 1.9
            case num if num in range(120, 150):
                return 1.8
            case num if num in range(150, 186):
                return 1.7
            case num if num in range(186, 230):
                return 1.6
            case num if num in range(230, 285):
                return 1.5
            case num if num in range(285, 358):
                return 1.4
            case num if num in range(358, 9999):
                return 1.3

        # (Voroth)
        # His
        # ATK
        # speed
        # scales
        # differnt
        # for some reason.
        #     2.6
        #     ATK
        #     interval
        #     base
        #     VOROTH
        #     only.
        # 1.9: 61 *
        # 1.8: 74 *
        # 1.7: 89 *
        # 1.6: 106 *
        # 1.5: 126 *
        # 1.4: 147 *
        # 1.3: 172 *
        # 1.2: 201 *
        # 1.1: 234 *
        # 1.0: 273 *
        # 0.9: 321 *
        # 0.8: 378 *
    if attack_interval == 2.5:
        match attack_speed_gear:
            case num if num in range(41, 58):
                return 2.1
            case num if num in range(58, 77):
                return 2.0
            case num if num in range(77, 101):
                return 1.9
            case num if num in range(101, 128):
                return 1.8
            case num if num in range(128, 161):
                return 1.7
            case num if num in range(161, 201):
                return 1.6
            case num if num in range(201, 251):
                return 1.5
            case num if num in range(251, 315):
                return 1.4
            case num if num in range(315, 400):
                return 1.3
            case num if num in range(400, 9999):
                return 1.2  # to be confirmed
    if attack_interval == 2.4:
        match attack_speed_gear:
            case num if num in range(43, 61):
                return 2.0
            case num if num in range(61, 82):
                return 1.9
            case num if num in range(82, 107):
                return 1.8
            case num if num in range(107, 137):
                return 1.7
            case num if num in range(137, 173):
                return 1.6
            case num if num in range(173, 220):
                return 1.5
            case num if num in range(220, 275):
                return 1.4
            case num if num in range(275, 351):
                return 1.3
            case num if num in range(351, 9999):
                return 1.2
    if attack_interval == 2.2:
        match attack_speed_gear:
            case num if num in range(47, 68):
                return 1.8
            case num if num in range(68, 93):
                return 1.7
            case num if num in range(93, 122):
                return 1.6
            case num if num in range(122, 159):
                return 1.5
            case num if num in range(159, 205):
                return 1.4
            case num if num in range(205, 264):
                return 1.3
            case num if num in range(264, 343):
                return 1.2
            case num if num in range(343, 9999):
                return 1.1
    if attack_interval == 2.1:
        match attack_speed_gear:
            case num if num in range(31, 50):
                return 1.8
            case num if num in range(50, 72):
                return 1.7
            case num if num in range(72, 99):
                return 1.6
            case num if num in range(99, 132):
                return 1.5
            case num if num in range(132, 173):
                return 1.4
            case num if num in range(173, 225):
                return 1.3
            case num if num in range(225, 295):
                return 1.2
            case num if num in range(295, 390):
                return 1.1
            case num if num in range(390, 9999):
                return 1.0  # to be confirmed
    if attack_interval == 2.0:
        match attack_speed_gear:
            case num if num in range(33, 53):
                return 1.7
            case num if num in range(53, 77):
                return 1.6
            case num if num in range(77, 107):
                return 1.5
            case num if num in range(107, 143):
                return 1.4
            case num if num in range(143, 190):
                return 1.3
            case num if num in range(190, 251):
                return 1.2
            case num if num in range(251, 334):
                return 1.1
            case num if num in range(334, 9999):
                return 1.0  # to be confirmed


class Collection(models.Model):

    @property
    def selected_faction(self) -> str:
        return self.selected_faction

    @selected_faction.setter
    def selected_faction(self, value):
        self.selected_faction = value

    hp50 = models.BooleanField(default=False)
    hp200_watcher = models.BooleanField(default=False)
    hp200_north = models.BooleanField(default=False)
    hp200_curse = models.BooleanField(default=False)
    hp200_nightmare = models.BooleanField(default=False)
    hp200_infernal = models.BooleanField(default=False)
    hp200_piercer = models.BooleanField(default=False)
    hp200_esoteric = models.BooleanField(default=False)
    hp200_chaos_dominion = models.BooleanField(default=False)
    hp200_arbiters = models.BooleanField(default=False)
    hp400 = models.BooleanField(default=False)
    rage_regen_atked = models.BooleanField(default=False)
    atk50_north = models.BooleanField(default=False)
    atk50_curse = models.BooleanField(default=False)
    atk50_nightmare = models.BooleanField(default=False)
    atk50_infernal = models.BooleanField(default=False)
    atk50_piercer = models.BooleanField(default=False)
    atk50_esoteric = models.BooleanField(default=False)
    atk50_chaos_dominion = models.BooleanField(default=False)
    atk50_arbiters = models.BooleanField(default=False)
    revival_time_minus_5 = models.BooleanField(default=False)
    rage_regen_basic_atk_1_nightmare = models.BooleanField(default=False)
    rage_regen_basic_atk_1_piercer = models.BooleanField(default=False)
    crit_rate_3 = models.BooleanField(default=False)
    crit_dmg_5 = models.BooleanField(default=False)
    init_rage_30 = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)


class Character(models.Model):
    rarity = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    heroclass = models.ForeignKey(HeroClass, on_delete=models.CASCADE)
    damagetype = models.ForeignKey(DamageType, on_delete=models.CASCADE)
    faction = models.ManyToManyField(Faction)
    name = models.CharField(max_length=250)
    health = models.IntegerField(default=0)
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    mRes = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    block = models.IntegerField(default=0)
    revival_time = models.IntegerField(default=60)
    attack_interval = models.FloatField(default=2.6)
    crit_dmg = models.IntegerField(default=150)
    attack_speed = models.IntegerField(default=100)
    rage_regen = models.IntegerField(default=0)
    rage_regen_auto = models.IntegerField(default=0)
    rage_regen_basic_atk = models.IntegerField(default=0)
    rage_regen_atked = models.IntegerField(default=0)

    @property
    def skill_multiplier(self) -> int:
        return 100

    @skill_multiplier.setter
    def skill_multiplier(self, value):
        self.skill_multiplier = value

    @property
    def defence_reduction(self) -> int:
        return 0

    @defence_reduction.setter
    def defence_reduction(self, value):
        self._defence_reduction = value

    def get_damage_per_attack(self, total_atk, ratio_crit_dmg, character, defence_reduction, ratio_crit):
        h = total_atk * (1 - 0.3) - (
            4826 if DamageType.DamageTypeEnum.MAGIC == character.damagetype.dmg_type else 5361
        ) / (1 + defence_reduction / 100)
        return max(
            (h + h * (ratio_crit_dmg - 1) * ratio_crit) * (character.skill_multiplier / 100),
            total_atk * ratio_crit_dmg * 0.0497,
        )

    @property
    def total_dps(self) -> str:
        # Based on NM4
        # armourType: "common",
        # physicalFlatReduction: 5361,
        # magicFlatReduction: 4826,
        # magicPercentageReduction: .3,
        # physicalPercentageReduction: .3
        character = self
        ratio_crit = min(character.total_crit_rate, 100) / 100
        ratio_crit_dmg = character.total_crit_dmg / 100
        total_akt = character.total_atk
        # no_crit_dmg = Decimal(self.get_damage_per_attack(total_akt, 1, character, defence_reduction, 0)).quantize(
        #    Decimal('.01'), rounding=ROUND_HALF_UP
        # )
        # crit_dmg = Decimal(
        #    self.get_damage_per_attack(total_akt, ratio_crit_dmg, character, defence_reduction, 1)
        # ).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
        return "{0:.2f}".format(
            self.get_damage_per_attack(total_akt, ratio_crit_dmg, character, self._defence_reduction, ratio_crit)
            / character.total_attack_interval
        )

    @total_dps.setter
    def total_dps(self, value):
        self.total_dps = value

    @property
    def hp_gear(self) -> int:
        hp_gear = 0
        if hasattr(self, "chestplate"):
            hp_gear += self.chestplate.main_stat_value
        if hasattr(self, "weapon"):
            hp_gear += hp_equipment(self.health, self.weapon)
        if hasattr(self, "chestplate"):
            hp_gear += hp_equipment(self.health, self.chestplate)
        if hasattr(self, "wristband"):
            hp_gear += hp_equipment(self.health, self.wristband)
        if hasattr(self, "amulet"):
            hp_gear += hp_equipment(self.health, self.amulet)
        if hasattr(self, "ring"):
            hp_gear += hp_equipment(self.health, self.ring)
        return int(hp_gear)

    @hp_gear.setter
    def hp_gear(self, value):
        self.hp_gear = value

    @property
    def hp_artifact(self) -> int:
        hp_artifact = 0
        if hasattr(self, "artifact"):
            hp_artifact += self.artifact.hp
        return int(hp_artifact)

    @hp_artifact.setter
    def hp_artifact(self, value):
        self.hp_artifact = value

    @property
    def hp_collection(self) -> int:
        hp_collection = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.WATCHER and collection.hp50:
                hp_collection += 50
            if (
                (faction.faction == Faction.FactionEnum.WATCHER and collection.hp200_watcher)
                or (faction.faction == Faction.FactionEnum.NORTH and collection.hp200_north)
                or (faction.faction == Faction.FactionEnum.NIGHTMARE and collection.hp200_nightmare)
                or (faction.faction == Faction.FactionEnum.CURSE and collection.hp200_curse)
                or (faction.faction == Faction.FactionEnum.INFERNAL and collection.hp200_infernal)
                or (faction.faction == Faction.FactionEnum.PIERCER and collection.hp200_piercer)
                or (faction.faction == Faction.FactionEnum.ESOTERIC and collection.hp200_esoteric)
                or (faction.faction == Faction.FactionEnum.CHAOS_DOMINION and collection.hp200_chaos_dominion)
                or (faction.faction == Faction.FactionEnum.ARBITERS and collection.hp200_arbiters)
            ):
                hp_collection += 200
            if faction.faction == Faction.FactionEnum.CHAOS_DOMINION and collection.hp400:
                hp_collection += 400
        return int(hp_collection)

    @hp_collection.setter
    def hp_collection(self, value):
        self.hp_collection = value

    @property
    def total_hp(self) -> int:
        return int(self.health + self.hp_gear + self.hp_artifact + self.hp_collection)

    @total_hp.setter
    def total_hp(self, value):
        self.total_hp = value

    @property
    def atk_gear(self) -> int:
        atk_gear = 0
        if hasattr(self, "weapon"):
            atk_gear += self.weapon.main_stat_value
            atk_gear += atk_equipment(self.attack, self.weapon)
        if hasattr(self, "chestplate"):
            atk_gear += atk_equipment(self.attack, self.chestplate)
        if hasattr(self, "weapon") and hasattr(self, "chestplate") and self.weapon.set_name == self.chestplate.set_name:
            if self.weapon.set_name in (Set2pEnum.CALAMITY, Set2pEnum.WARLORD):
                atk_gear += self.attack * 25 / 100
        if hasattr(self, "wristband"):
            atk_gear += atk_equipment(self.attack, self.wristband)
        if hasattr(self, "amulet"):
            atk_gear += atk_equipment(self.attack, self.amulet)
        if hasattr(self, "ring"):
            atk_gear += atk_equipment(self.attack, self.ring)
        return int(atk_gear)

    @atk_gear.setter
    def atk_gear(self, value):
        self.atk_gear = value

    @property
    def atk_artifact(self) -> int:
        atk_artifact = 0
        if hasattr(self, "artifact"):
            atk_artifact += self.artifact.atk
        return int(atk_artifact)

    @atk_artifact.setter
    def atk_artifact(self, value):
        self.atk_artifact = value

    @property
    def atk_collection(self) -> int:
        atk_collection = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if (
                (faction.faction == Faction.FactionEnum.NORTH and collection.atk50_north)
                or (faction.faction == Faction.FactionEnum.NIGHTMARE and collection.atk50_nightmare)
                or (faction.faction == Faction.FactionEnum.CURSE and collection.atk50_curse)
                or (faction.faction == Faction.FactionEnum.INFERNAL and collection.atk50_infernal)
                or (faction.faction == Faction.FactionEnum.PIERCER and collection.atk50_piercer)
                or (faction.faction == Faction.FactionEnum.ESOTERIC and collection.atk50_esoteric)
                or (faction.faction == Faction.FactionEnum.CHAOS_DOMINION and collection.atk50_chaos_dominion)
                or (faction.faction == Faction.FactionEnum.ARBITERS and collection.atk50_arbiters)
            ):
                atk_collection += 50
        return int(atk_collection)

    @atk_collection.setter
    def atk_collection(self, value):
        self.atk_collection = value

    @property
    def total_atk(self) -> int:
        return int(self.attack + self.atk_gear + self.atk_artifact + self.atk_collection)

    @total_atk.setter
    def total_atk(self, value):
        self.total_atk = value

    @property
    def def_gear(self) -> int:
        def_gear = 0
        if hasattr(self, "weapon"):
            def_gear += def_equipment(self.defense, self.weapon)
        if hasattr(self, "chestplate"):
            def_gear += def_equipment(self.defense, self.chestplate)
        if hasattr(self, "wristband"):
            def_gear += def_equipment(self.defense, self.wristband)
        if hasattr(self, "amulet"):
            def_gear += def_equipment(self.defense, self.amulet)
        if hasattr(self, "ring"):
            def_gear += def_equipment(self.defense, self.ring)
        return int(def_gear)

    @def_gear.setter
    def def_gear(self, value):
        self.def_gear = value

    @property
    def total_def(self) -> int:
        return int(self.defense + self.def_gear)

    @total_def.setter
    def total_def(self, value):
        self.total_def = value

    @property
    def total_mRes(self) -> int:
        return int(self.mRes)

    @total_mRes.setter
    def total_mRes(self, value):
        self.total_mRes = value

    @property
    def total_cost(self) -> int:
        return int(self.cost)

    @total_cost.setter
    def total_cost(self, value):
        self.total_cost = value

    @property
    def total_block(self) -> int:
        return int(self.block)

    @total_block.setter
    def total_block(self, value):
        self.total_block = value

    @property
    def revival_time_collection(self) -> int:
        revival_time = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.NORTH and collection.revival_time_minus_5:
                revival_time -= 5
        return int(revival_time)

    @revival_time_collection.setter
    def revival_time_collection(self, value):
        self.revival_time_collection = value

    @property
    def total_revival_time(self) -> int:
        return int(self.revival_time + self.revival_time_collection)

    @total_revival_time.setter
    def total_revival_time(self, value):
        self.total_revival_time = value

    @property
    def attack_interval_gear(self) -> float:
        atk_int_equip: float = attack_interval_equipment(self.attack_interval, self.attack_speed_gear)
        if atk_int_equip is None:
            return 0
        else:
            return round(self.attack_interval - atk_int_equip, 6)

    @attack_interval_gear.setter
    def attack_interval_gear(self, value):
        self.attack_interval_gear = value

    @property
    def total_attack_interval(self) -> float:
        return round(self.attack_interval - self.attack_interval_gear, 6)

    @total_attack_interval.setter
    def total_attack_interval(self, value):
        self.total_attack_interval = value

    @property
    def attack_speed_gear(self) -> int:
        crt_attack_speed_gear = 0
        if hasattr(self, "weapon"):
            crt_attack_speed_gear += attack_speed_equipment(self.weapon)
        if hasattr(self, "chestplate"):
            crt_attack_speed_gear += attack_speed_equipment(self.chestplate)
        if hasattr(self, "weapon") and hasattr(self, "chestplate") and self.weapon.set_name == self.chestplate.set_name:
            if self.weapon.set_name == Set2pEnum.WARLORD:
                crt_attack_speed_gear += 30
            if self.weapon.set_name == Set2pEnum.WHIRLWIND:
                crt_attack_speed_gear += 75
        if hasattr(self, "wristband"):
            crt_attack_speed_gear += attack_speed_equipment(self.wristband)
        if hasattr(self, "amulet"):
            crt_attack_speed_gear += attack_speed_equipment(self.amulet)
        if hasattr(self, "ring"):
            crt_attack_speed_gear += attack_speed_equipment(self.ring)
        return int(crt_attack_speed_gear)

    @attack_speed_gear.setter
    def attack_speed_gear(self, value):
        self.attack_speed_gear = value

    @property
    def total_attack_speed(self) -> int:
        return self.attack_speed + self.attack_speed_gear

    @total_attack_speed.setter
    def total_attack_speed(self, value):
        self.total_attack_speed = value

    @property
    def crit_rate_gear(self) -> int:
        crit_rate_gear = 0
        if hasattr(self, "weapon"):
            crit_rate_gear += crit_rate_equipment(self.weapon)
        if hasattr(self, "chestplate"):
            crit_rate_gear += crit_rate_equipment(self.chestplate)
        if hasattr(self, "wristband"):
            crit_rate_gear += crit_rate_equipment(self.wristband)
        if hasattr(self, "amulet"):
            crit_rate_gear += crit_rate_equipment(self.amulet)
        if hasattr(self, "ring"):
            crit_rate_gear += crit_rate_equipment(self.ring)
        return int(crit_rate_gear)

    @crit_rate_gear.setter
    def crit_rate_gear(self, value):
        self.crit_rate_gear = value

    @property
    def crit_rate_collection(self) -> int:
        crt_crit_rate_collection = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.CURSE and collection.crit_rate_3:
                crt_crit_rate_collection += 3
        return int(crt_crit_rate_collection)

    @crit_rate_collection.setter
    def crit_rate_collection(self, value):
        self.crit_rate_collection = value

    @property
    def total_crit_rate(self) -> int:
        return self.crit_rate_gear

    @total_crit_rate.setter
    def total_crit_rate(self, value):
        self.total_crit_rate = value

    @property
    def crit_dmg_gear(self) -> int:
        crt_crit_dmg_gear = 0
        if hasattr(self, "weapon"):
            crt_crit_dmg_gear += crit_dmg_equipment(self.weapon)
        if hasattr(self, "chestplate"):
            crt_crit_dmg_gear += crit_dmg_equipment(self.chestplate)
        if hasattr(self, "wristband"):
            crt_crit_dmg_gear += crit_dmg_equipment(self.wristband)
        if hasattr(self, "amulet"):
            crt_crit_dmg_gear += crit_dmg_equipment(self.amulet)
        if hasattr(self, "ring"):
            crt_crit_dmg_gear += crit_dmg_equipment(self.ring)
        return int(crt_crit_dmg_gear)

    @crit_dmg_gear.setter
    def crit_dmg_gear(self, value):
        self.crit_dmg_gear = value

    @property
    def crit_dmg_collection(self) -> int:
        crt_crit_dmg_collection = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.INFERNAL and collection.crit_dmg_5:
                crt_crit_dmg_collection += 5
        return int(crt_crit_dmg_collection)

    @crit_dmg_collection.setter
    def crit_dmg_collection(self, value):
        self.crit_dmg_collection = value

    @property
    def total_crit_dmg(self) -> int:
        return int(self.crit_dmg + self.crit_dmg_gear)

    @total_crit_dmg.setter
    def total_crit_dmg(self, value):
        self.total_crit_dmg = value

    @property
    def heal_effect_gear(self) -> int:
        crt_healing_effect_gear = 0
        if hasattr(self, "weapon"):
            crt_healing_effect_gear += healing_effect_equipment(self.weapon)
        if hasattr(self, "chestplate"):
            crt_healing_effect_gear += healing_effect_equipment(self.chestplate)
        if hasattr(self, "wristband"):
            crt_healing_effect_gear += healing_effect_equipment(self.wristband)
        if hasattr(self, "amulet"):
            crt_healing_effect_gear += healing_effect_equipment(self.amulet)
        if hasattr(self, "ring"):
            crt_healing_effect_gear += healing_effect_equipment(self.ring)
        return int(crt_healing_effect_gear)

    @heal_effect_gear.setter
    def heal_effect_gear(self, value):
        self.heal_effect_gear = value

    @property
    def total_heal_effect(self) -> int:
        return int(self.heal_effect_gear)

    @total_heal_effect.setter
    def total_heal_effect(self, value):
        self.total_heal_effect = value

    @property
    def rage_regen_gear(self) -> int:
        crt_rage_regen_gear = 0
        if hasattr(self, "weapon"):
            crt_rage_regen_gear += rage_regen_equipment(self.weapon)
        if hasattr(self, "chestplate"):
            crt_rage_regen_gear += rage_regen_equipment(self.chestplate)
        if hasattr(self, "wristband"):
            crt_rage_regen_gear += rage_regen_equipment(self.wristband)
        if hasattr(self, "amulet"):
            crt_rage_regen_gear += rage_regen_equipment(self.amulet)
        if hasattr(self, "ring"):
            crt_rage_regen_gear += rage_regen_equipment(self.ring)
        return int(crt_rage_regen_gear)

    @rage_regen_gear.setter
    def rage_regen_gear(self, value):
        self.rage_regen_gear = value

    @property
    def rage_regen_collection(self) -> int:
        crt_rage_regen_collection = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.ESOTERIC and collection.init_rage_30:
                crt_rage_regen_collection += 30
        return int(crt_rage_regen_collection)

    @rage_regen_collection.setter
    def rage_regen_collection(self, value):
        self.rage_regen_collection = value

    @property
    def total_rage_regen(self) -> int:
        return int(self.rage_regen_gear)

    @total_rage_regen.setter
    def total_rage_regen(self, value):
        self.total_rage_regen = value

    @property
    def total_rage_regen_auto(self) -> int:
        return int(self.rage_regen_auto)

    @total_rage_regen_auto.setter
    def total_rage_regen_auto(self, value):
        self.total_rage_regen_auto = value

    @property
    def rage_regen_basic_atk_collection(self) -> int:
        rage_regen_basic_atk = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if (faction.faction == Faction.FactionEnum.NIGHTMARE and collection.rage_regen_basic_atk_1_nightmare) or (
                faction.faction == Faction.FactionEnum.PIERCER and collection.rage_regen_basic_atk_1_piercer
            ):
                rage_regen_basic_atk += 1
        return int(rage_regen_basic_atk)

    @rage_regen_basic_atk_collection.setter
    def rage_regen_basic_atk_collection(self, value):
        self.rage_regen_basic_atk_collection = value

    @property
    def total_rage_regen_basic_atk(self) -> int:
        return int(self.rage_regen_basic_atk + self.rage_regen_basic_atk_collection)

    @total_rage_regen_basic_atk.setter
    def total_rage_regen_basic_atk(self, value):
        self.total_rage_regen_basic_atk = value

    @property
    def rage_regen_atked_collection(self) -> int:
        rage_regen_atked = 0
        factions = Faction.objects.filter(character=self.id)
        for faction in factions:
            collection = Collection.objects.get(faction=faction)
            if faction.faction == Faction.FactionEnum.WATCHER and collection.rage_regen_atked:
                rage_regen_atked += 1
        return int(rage_regen_atked)

    @rage_regen_atked_collection.setter
    def rage_regen_atked_collection(self, value):
        self.rage_regen_atked_collection = value

    @property
    def total_rage_regen_atked(self) -> int:
        return int(self.rage_regen_atked + self.rage_regen_atked_collection)

    @total_rage_regen_atked.setter
    def total_rage_regen_atked(self, value):
        self.total_rage_regen_atked = value

    def __str__(self):
        return self.name


class Pantheon(models.Model):
    atk_bonus = models.FloatField(default=0)
    hp_bonus = models.FloatField(default=0)
    rage_regen = models.FloatField(default=0)
    crit_dmg = models.FloatField(default=0)
    healing_effect = models.FloatField(default=0)
    atk_spd = models.FloatField(default=0)
    def_bonus = models.FloatField(default=0)
    mRes_bonus = models.FloatField(default=0)
    crit_rate = models.FloatField(default=0)
    ragen_regen_auto = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Artifact(models.Model):
    atk = models.IntegerField(default=0)
    hp = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character = models.OneToOneField(Character, on_delete=models.CASCADE, null=True, blank=True)
