from django.shortcuts import render, redirect
from myapp.models import Food, Consume


def index(request):
    if request.method == "POST":
        food_name = request.POST["food_consume"]
        user = request.user

        food = Food.objects.get(name=food_name)

        user_food = Consume(user=user, food_consume=food)
        user_food.save()
        
        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
        
    consumed_food_by_user = Consume.objects.filter(user=request.user)
    return render(request, "myapp/index.html", {"foods": foods, "consumed_food_by_user":consumed_food_by_user})


def delete_consume(request, id):
    consumed_item = Consume.objects.get(pk=id)
    consumed_item.delete()
    return redirect("index")