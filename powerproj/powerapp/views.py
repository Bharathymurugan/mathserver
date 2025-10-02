from django.shortcuts import render
def calculator(request):
    power= None
    if request.method == "POST":
        I=float(request.POST.get("I"))
        R=float(request.POST.get("R"))
        power=I**2 *R
        print(f"Enter Current value(in amperes): {I}, Enter Resistance value(in ohm): {R}, Power={power:.2f}")
        return render(request, 'result.html', {'power': power, 'I': I, 'R': R})
    return render(request, 'power.html', {'power':power})
# Create your views here.
