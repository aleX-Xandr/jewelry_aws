from django.utils.safestring import mark_safe
from paypal.standard.forms import PayPalPaymentsForm

class CustomPayPalPaymentsForm(PayPalPaymentsForm):
    def get_html_submit_element(self):
        return mark_safe("""<button type="submit" id="submit_paypal" style="background: transparent; border: unset; color: #fff; font-size: 17px; font-weight: 700; line-height: 18.46px;">Procedi all’acquisto</button>""")