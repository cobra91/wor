from django.shortcuts import redirect, render
from django.views import generic

from .forms import AmuletForm, CharacterForm, ChestplateForm, RingForm, WeaponForm, WristbandForm
from .models import Amulet, Character, Chestplate, Ring, Weapon, Wristband


def index_show_view(request):
    template_name = "wor/base.html"
    return render(request, template_name)


class CharacterView(generic.ListView):
    template_name = "wor/show/characters.html"
    context_object_name = "latest_character_list"

    def get_queryset(self):
        return Character.objects.order_by("-name")


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
        if form.is_valid():
            form.save()
            return redirect("wor:show_ring_url")
    template_name = "wor/form/ring_form.html"
    context = {"form": form}
    return render(request, template_name, context)


def weapon_show_view(request):
    weapons = Weapon.objects.all()
    template_name = "wor/show/weapons.html"
    context = {"weapons": weapons}
    return render(request, template_name, context)


def chestplate_show_view(request):
    chestplates = Chestplate.objects.all()
    template_name = "wor/show/chestplates.html"
    context = {"chestplates": chestplates}
    return render(request, template_name, context)


def wristband_show_view(request):
    wristbands = Wristband.objects.all()
    template_name = "wor/show/wristbands.html"
    context = {"wristbands": wristbands}
    return render(request, template_name, context)


def amulet_show_view(request):
    amulets = Amulet.objects.all()
    template_name = "wor/show/amulets.html"
    context = {"amulets": amulets}
    return render(request, template_name, context)


def ring_show_view(request):
    rings = Ring.objects.all()
    template_name = "wor/show/rings.html"
    context = {"rings": rings}
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
    ring = Ring.objects.get(id=f_id)
    if request.method == "POST":
        form = RingForm(request.POST, instance=ring)
        if form.is_valid():
            form.save()
            return redirect("wor:show_ring_url")
    template_name = "wor/form/ring_form.html"
    form = RingForm(instance=ring)
    context = {"form": form}
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
