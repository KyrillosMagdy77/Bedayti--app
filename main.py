import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة (تم التعديل لتناسب شاشة الموبايل)
    page.title = "حاسبة القروض"
    page.rtl = True  # تفعيل دعم اللغة العربية
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO  # تفعيل السكرول للموبايل

    # عنوان التطبيق
    title = ft.Text("حاسبة القروض", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900)

    # حقول الإدخال
    amount_input = ft.TextField(label="مبلغ القرض", keyboard_type=ft.KeyboardType.NUMBER, icon=ft.icons.MONETIZATION_ON)
    months_input = ft.TextField(label="عدد الأشهر", keyboard_type=ft.KeyboardType.NUMBER, icon=ft.icons.CALENDAR_MONTH)

    # نصوص النتائج
    fees_text = ft.Text("المصاريف الإدارية: 0", size=18, weight=ft.FontWeight.W_500)
    installment_text = ft.Text("القسط الشهري: 0", size=18, weight=ft.FontWeight.W_500, color=ft.colors.GREEN_700)
    total_text = ft.Text("إجمالي المبلغ: 0", size=18, weight=ft.FontWeight.W_500, color=ft.colors.RED_700)

    # دالة الحساب التي تعمل عند الضغط على الزر
    def calculate_click(e):
        try:
            loan_amount = float(amount_input.value)
            months = int(months_input.value)

            admin_fees = loan_amount * 0.04
            
            if loan_amount <= 100000:
                interest_rate = 0.025
            else:
                interest_rate = 0.023333333333
            
            total_interest = loan_amount * interest_rate * months
            total_to_pay = loan_amount + total_interest
            monthly_installment = total_to_pay / months

            fees_text.value = f"المصاريف الإدارية: {admin_fees:,.2f}"
            installment_text.value = f"القسط الشهري: {monthly_installment:,.2f}"
            total_text.value = f"إجمالي المبلغ بالفوائد: {total_to_pay:,.2f}"
            
        except ValueError:
            fees_text.value = "خطأ: الرجاء إدخال أرقام صحيحة!"
            installment_text.value = ""
            total_text.value = ""

        page.update()

    # زر الحساب
    calc_button = ft.ElevatedButton(
        text="احسب الآن", 
        icon=ft.icons.CALCULATE,
        on_click=calculate_click,
        style=ft.ButtonStyle(padding=15)
    )

    # ترتيب العناصر في الصفحة مع مسافات آمنة
    page.add(
        ft.SafeArea(
            ft.Column([
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                title,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                amount_input,
                months_input,
                ft.Divider(height=10, color=ft.colors.TRANSPARENT),
                calc_button,
                ft.Divider(height=20),
                fees_text,
                installment_text,
                total_text
            ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

ft.app(target=main) 
