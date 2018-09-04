"""Testes da funcionalidade calculo da media."""

from behave import given, when, then

from sistema import media


@given('os números 2 e 4')
def given_dois_numeros(context):
    """Dado que o sistema tenha dois valores."""
    context.num1 = 2
    context.num2 = 4


@when('calculo a media de dois numeros')
def when_calcula_media(context):
    """Forca o calculo da media."""
    a = context.num1
    b = context.num2
    context.resultado = media(a, b)


@then('o resultado e 3')
def then_verifica_media(context):
    """Verifica o resultado do calculo da media."""
    assert context.resultado == 3
