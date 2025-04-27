import flet as ft
from decimal import Decimal
import asyncio
import get_cours


cours = get_cours.update_course() # [USD, EUR, GBP]

def main(page: ft.Page):
    async def click(e):
        input_value = Decimal(converted_sum.value) if converted_sum.value else Decimal(0)
        result = Decimal(0)
        if currency.value == "USD":
            result = input_value * Decimal(cours[0])
        elif currency.value == "EUR":
            result = input_value * Decimal(cours[1])
        elif currency.value == "GBP":
            result = input_value * Decimal(cours[2])
        page.add(ft.Text(f"Сума в гривнях(UAH/{currency.value}): {round(result, 2)}"))


    currency = ft.Dropdown(width=100, options=[
        ft.dropdown.Option("USD"),
        ft.dropdown.Option("EUR"),
        ft.dropdown.Option("GBP"),
    ])

    page.title = "Конвертер валют"
    page.add(ft.Text("Курси валют к гривні"), ft.Text(f"USD: {cours[0]}\nEUR: {cours[1]}\nGBP: {cours[2]}"))
    converted_sum = ft.TextField(hint_text="Сума для конвертації", width=300)
    page.add(ft.Row([converted_sum, currency, ft.ElevatedButton("Конвертувати", on_click=click)]))



ft.app(target=main, view=ft.WEB_BROWSER)
