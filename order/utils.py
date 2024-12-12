from django.utils.safestring import mark_safe
from paypal.standard.forms import PayPalPaymentsForm

class CustomPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return mark_safe("""<button type="submit">Procedi all&rsquo;acquisto</button>""")