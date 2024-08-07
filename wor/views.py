from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import (
    AmuletForm,
    CharacterForm,
    ChestplateForm,
    CompareEquipmentForm,
    RingForm,
    WeaponForm,
    WristbandForm,
    PantheonForm,
    ArtifactForm,
    CollectionForm,
    WatcherCollectionForm,
    NorthCollectionForm,
    CurseCollectionForm,
    InfernalCollectionForm,
    NightmareCollectionForm,
    ChaosDominionCollectionForm,
    PiercerCollectionForm,
    EsotericCollectionForm,
    ArbitersCollectionForm,
)
from .models import Amulet, Character, Chestplate, Ring, Weapon, Wristband, Pantheon, Artifact, Collection, Faction

resultlist: list[object] = []


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "wor/registration/signup.html"


@login_required
def index_show_view(request):
    template_name = "wor/base.html"
    return render(request, template_name)


def compare_equipment_form_view(request):
    template_name = "wor/form/compare_equipment_form.html"
    if request.method == "POST":
        form = CompareEquipmentForm(request.POST)
        if form.is_valid():
            context = {
                "form": form,
                "character_list": Character.objects.order_by("name"),
                "result_list": form.compare(),
                "characterEquipList": form.characterEquipList,
            }
            return render(request, template_name, context)
    if request.method == "GET" and len(CompareEquipmentForm(request.GET).resultlist) > 0:
        form = CompareEquipmentForm(request.GET)
        context = {
            "result": form.resultlist[int(request.GET.get("result_id"))] if request.GET.get("result_id") else None,
            "form": form,
            "character_list": Character.objects.order_by("name"),
            "result_list": form.resultlist,
            "characterEquipList": form.characterEquipList,
        }
        CompareEquipmentForm(request.GET).resultlist = []
        return render(request, template_name, context)
    form = CompareEquipmentForm()
    context = {"form": form, "character_list": Character.objects.order_by("name")}
    return render(request, template_name, context)


class CharacterView(generic.ListView):
    template_name = "wor/show/characters.html"
    context_object_name = "character_list"

    def get_queryset(self):
        return Character.objects.order_by("name")


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = "wor/detail/character_detail.html"


def character_form_view(request):
    form = CharacterForm()
    if request.method == "POST":
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wor:show_character_url")
    template_name = "wor/form/character_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def weapon_form_view(request):
    form = WeaponForm()
    if request.method == "POST":
        form = WeaponForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_weapon_url")
    template_name = "wor/form/weapon_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def chestplate_form_view(request):
    form = ChestplateForm()
    if request.method == "POST":
        form = ChestplateForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_chestplate_url")
    template_name = "wor/form/chestplate_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def wristband_form_view(request):
    form = WristbandForm()
    if request.method == "POST":
        form = WristbandForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_wristband_url")
    template_name = "wor/form/wristband_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def amulet_form_view(request):
    form = AmuletForm()
    if request.method == "POST":
        form = AmuletForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_amulet_url")
    template_name = "wor/form/amulet_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def ring_form_view(request):
    form = RingForm()
    if request.method == "POST":
        form = RingForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_ring_url")
    template_name = "wor/form/ring_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def pantheon_form_view(request):
    form = PantheonForm()
    if request.method == "POST":
        form = PantheonForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_pantheon_url")
    template_name = "wor/form/pantheon_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def artifact_form_view(request):
    form = ArtifactForm()
    if request.method == "POST":
        form = ArtifactForm(request.POST)
        user: User = get_user(request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_artifact_url")
    template_name = "wor/form/artifact_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def collection_form_view(request):
    form = CollectionForm()
    user: User = get_user(request)
    if request.method == "POST":
        updated_request = request.POST.copy()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.WATCHER)
        updated_request.update({'faction': faction})
        form = WatcherCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.NORTH)
        updated_request.update({'faction': faction})
        form = NorthCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.CURSE)
        updated_request.update({'faction': faction})
        form = CurseCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.NIGHTMARE)
        updated_request.update({'faction': faction})
        form = NightmareCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.INFERNAL)
        updated_request.update({'faction': faction})
        form = InfernalCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.PIERCER)
        updated_request.update({'faction': faction})
        form = PiercerCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.ESOTERIC)
        updated_request.update({'faction': faction})
        form = EsotericCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.CHAOS_DOMINION)
        updated_request.update({'faction': faction})
        form = ChaosDominionCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.ARBITERS)
        updated_request.update({'faction': faction})
        form = ArbitersCollectionForm(updated_request)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
        return redirect("wor:show_collection_url")
    template_name = "wor/form/collection_form.html"
    factions = Faction.objects.all()
    collections = Collection.objects.filter(user_id=user.id)
    context = {"form": form, "factions": factions, "collections": collections}
    return render(request, template_name, context)


def weapon_show_view(request):
    user: User = get_user(request)
    weapons = Weapon.objects.all().filter(user_id=user.id)
    template_name = "wor/show/weapons.html"
    context = {"weapons": weapons}
    return render(request, template_name, context)


def chestplate_show_view(request):
    user: User = get_user(request)
    chestplates = Chestplate.objects.all().filter(user_id=user.id)
    template_name = "wor/show/chestplates.html"
    context = {"chestplates": chestplates}
    return render(request, template_name, context)


def wristband_show_view(request):
    user: User = get_user(request)
    wristbands = Wristband.objects.all().filter(user_id=user.id)
    template_name = "wor/show/wristbands.html"
    context = {"wristbands": wristbands}
    return render(request, template_name, context)


def amulet_show_view(request):
    user: User = get_user(request)
    amulets = Amulet.objects.all().filter(user_id=user.id)
    template_name = "wor/show/amulets.html"
    context = {"amulets": amulets}
    return render(request, template_name, context)


def ring_show_view(request):
    user: User = get_user(request)
    rings = Ring.objects.all().filter(user_id=user.id)
    template_name = "wor/show/rings.html"
    context = {"rings": rings}
    return render(request, template_name, context)


def pantheon_show_view(request):
    user: User = get_user(request)
    pantheon = Pantheon.objects.get(user_id=user.id)
    template_name = "wor/show/pantheon.html"
    context = {"pantheon": pantheon}
    return render(request, template_name, context)


def artifact_show_view(request):
    user: User = get_user(request)
    artifacts = Artifact.objects.all().filter(user_id=user.id)
    template_name = "wor/show/artifacts.html"
    context = {"artifacts": artifacts}
    return render(request, template_name, context)


def collection_show_view(request):
    user: User = get_user(request)
    collections = Collection.objects.all().filter(user_id=user.id)
    template_name = "wor/show/collections.html"
    context = {"collections": collections}
    return render(request, template_name, context)


def character_update_view(request, f_id):
    character = Character.objects.get(id=f_id)
    if request.method == "POST":
        form = CharacterForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            return redirect("wor:show_character_url")
    template_name = "wor/form/character_form.html"
    form = CharacterForm(instance=character)
    context = {"form": form}
    return render(request, template_name, context)


def weapon_update_view(request, f_id):
    weapon = Weapon.objects.get(id=f_id)
    if request.method == "POST":
        form = WeaponForm(request.POST, instance=weapon)
        if form.is_valid():
            form.save()
            return redirect("wor:show_weapon_url")
    template_name = "wor/form/weapon_form.html"
    form = WeaponForm(instance=weapon)
    context = {"form": form}
    return render(request, template_name, context)


def chestplate_update_view(request, f_id):
    chestplate = Chestplate.objects.get(id=f_id)
    if request.method == "POST":
        form = ChestplateForm(request.POST, instance=chestplate)
        if form.is_valid():
            form.save()
            return redirect("wor:show_chestplate_url")
    template_name = "wor/form/chestplate_form.html"
    form = ChestplateForm(instance=chestplate)
    context = {"form": form}
    return render(request, template_name, context)


def wristband_update_view(request, f_id):
    wristband = Wristband.objects.get(id=f_id)
    if request.method == "POST":
        form = WristbandForm(request.POST, instance=wristband)
        if form.is_valid():
            form.save()
            return redirect("wor:show_wristband_url")
    template_name = "wor/form/wristband_form.html"
    form = WristbandForm(instance=wristband)
    context = {"form": form}
    return render(request, template_name, context)


def amulet_update_view(request, f_id):
    amulet = Amulet.objects.get(id=f_id)
    if request.method == "POST":
        form = AmuletForm(request.POST, instance=amulet)
        if form.is_valid():
            form.save()
            return redirect("wor:show_amulet_url")
    template_name = "wor/form/amulet_form.html"
    form = AmuletForm(instance=amulet)
    context = {"form": form}
    return render(request, template_name, context)


def ring_update_view(request, f_id):
    user: User = get_user(request)
    ring = Ring.objects.get(user_id=user.id, id=f_id)
    if request.method == "POST":
        form = RingForm(request.POST, instance=ring)
        if form.is_valid():
            form.save()
            return redirect("wor:show_ring_url")
    template_name = "wor/form/ring_form.html"
    form = RingForm(instance=ring)
    context = {"form": form}
    return render(request, template_name, context)


def pantheon_update_view(request, f_id):
    user: User = get_user(request)
    pantheon = Pantheon.objects.get(user_id=user.id, id=f_id)
    if request.method == "POST":
        form = PantheonForm(request.POST, instance=pantheon)
        if form.is_valid():
            form.save()
            return redirect("wor:show_pantheon_url")
    template_name = "wor/form/pantheon_form.html"
    form = PantheonForm(instance=pantheon)
    context = {"form": form}
    return render(request, template_name, context)


def artifact_update_view(request, f_id):
    user: User = get_user(request)
    artifact = Artifact.objects.get(user_id=user.id, id=f_id)
    if request.method == "POST":
        form = ArtifactForm(request.POST, instance=artifact)
        if form.is_valid():
            form.save()
            return redirect("wor:show_artifact_url")
    template_name = "wor/form/artifact_form.html"
    form = ArtifactForm(instance=artifact)
    context = {"form": form}
    return render(request, template_name, context)


def collection_update_view(request, f_id):
    user: User = get_user(request)
    collections: Collection = Collection.objects.get(user_id=user.id, id=f_id)
    factions = Faction.objects.all().filter(id=collections.faction.id)
    if request.method == "POST":
        updated_request = request.POST.copy()
        if request.POST['selected_faction'] == Faction.FactionEnum.WATCHER:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.WATCHER)
            updated_request.update({'faction': faction})
            form = WatcherCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.NORTH:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.NORTH)
            updated_request.update({'faction': faction})
            form = NorthCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.CURSE:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.CURSE)
            updated_request.update({'faction': faction})
            form = CurseCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.NIGHTMARE:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.NIGHTMARE)
            updated_request.update({'faction': faction})
            form = NightmareCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.INFERNAL:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.INFERNAL)
            updated_request.update({'faction': faction})
            form = InfernalCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.PIERCER:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.PIERCER)
            updated_request.update({'faction': faction})
            form = PiercerCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.ESOTERIC:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.ESOTERIC)
            updated_request.update({'faction': faction})
            form = EsotericCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.CHAOS_DOMINION:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.CHAOS_DOMINION)
            updated_request.update({'faction': faction})
            form = ChaosDominionCollectionForm(updated_request, instance=collections)
        elif request.POST['selected_faction'] == Faction.FactionEnum.ARBITERS:
            faction: Faction = Faction.objects.get(faction=Faction.FactionEnum.ARBITERS)
            updated_request.update({'faction': faction})
            form = ArbitersCollectionForm(updated_request, instance=collections)
        form.user = user
        form.instance.user_id = user.id
        if form.is_valid():
            form.save()
            return redirect("wor:show_collection_url")
    template_name = "wor/form/collection_form.html"
    form = CollectionForm(instance=collections)
    context = {"form": form, "factions": factions, "collections": collections}
    return render(request, template_name, context)


def weapon_delete_view(request, f_id):
    obj = Weapon.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_weapon_url")
    template_name = "wor/delete/del_weapon.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def chestplate_delete_view(request, f_id):
    obj = Chestplate.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_chestplate_url")
    template_name = "wor/delete/del_chestplate.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def wristband_delete_view(request, f_id):
    obj = Wristband.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_wristband_url")
    template_name = "wor/delete/del_wristband.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def amulet_delete_view(request, f_id):
    obj = Amulet.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_amulet_url")
    template_name = "wor/delete/del_amulet.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def ring_delete_view(request, f_id):
    obj = Ring.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_ring_url")
    template_name = "wor/delete/del_ring.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def artifact_delete_view(request, f_id):
    obj = Artifact.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("wor:show_artifact_url")
    template_name = "wor/delete/del_artifact.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def weapon_detail(request, id):
    weapon = Weapon.objects.get(id=id)
    return render(request, "wor/detail/weapon_detail.html", {"weapon": weapon})


def chestplate_detail(request, id):
    chestplate = Chestplate.objects.get(id=id)
    return render(request, "wor/detail/chestplate_detail.html", {"chestplate": chestplate})


def wristband_detail(request, id):
    wristband = Wristband.objects.get(id=id)
    return render(request, "wor/detail/wristband_detail.html", {"wristband": wristband})


def amulet_detail(request, id):
    amulet = Amulet.objects.get(id=id)
    return render(request, "wor/detail/amulet_detail.html", {"amulet": amulet})


def ring_detail(request, id):
    ring = Ring.objects.get(id=id)
    return render(request, "wor/detail/ring_detail.html", {"ring": ring})
