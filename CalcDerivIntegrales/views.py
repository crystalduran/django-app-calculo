from django.shortcuts import render
from sympy import *

# Create your views here.

def calcular(request):
    derivada_resultado = None
    integral_resultado = None
    punto_evaluacion = 0
    a = 0
    b = 0
    f_LatexDerivada = None
    f_LatexIntegralIndefinida = None

    if request.method == 'POST':
        if 'calcularDerivadaBtn' in request.POST:
            derivada_input = request.POST['functionDerivada']
            try:
                f_derivada = sympify(derivada_input)
                x = symbols('x')
                derivada_resultado = diff(f_derivada, x)
                derivada_resultado = latex(derivada_resultado)
                f_LatexDerivada = latex(f_derivada)
            except SympifyError:
                derivada_resultado = "Error: Función inválida"
                f_LatexDerivada =  ""
        elif 'calcularIntegralIndefinidaBtn' in request.POST:
            integral_input = request.POST['functionIntegralIndefinida']
            try:
                f_integralIndefinida = sympify(integral_input)
                x = symbols('x')
                integral_resultado = integrate(f_integralIndefinida, x)
                integral_resultado = latex(integral_resultado)
                f_LatexIntegralIndefinida = latex(f_integralIndefinida)
            except SympifyError:
                integral_resultado = "Error: Función inválida"
                f_LatexIntegralIndefinida =  ""
        


        """
        if 'derivada_form' in request.POST:
            derivada_form = DerivativeForm(request.POST)
                x = symbols('x')
                expr = sympify(funcion)
                derivada_resultado = diff(expr, x)
                #derivada_resultado = diff(expr, x).subs(x, evaluation_point)
        elif 'integral_form' in request.POST:
            integral_form = IntegralForm(request.POST)
            if integral_form.is_valid():
                funcion = integral_form.cleaned_data['function']
                #lower_limit = integral_form.cleaned_data['lower_limit']
                #upper_limit = integral_form.cleaned_data['upper_limit']

                x = symbols('x')
                expr = sympify(funcion)
                integral_resultado = integrate(expr, x)
        """

    context = {'derivative_result': derivada_resultado, 'integral_result' : integral_resultado,'f_derivada' : f_LatexDerivada, 'f_integralIndefinida': f_LatexIntegralIndefinida}
    return render(request,'index.html',context)
    
    