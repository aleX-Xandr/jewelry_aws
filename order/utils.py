from django.utils.html import format_html
from paypal.standard.forms import PayPalPaymentsForm

class CustomPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return format_html(
            """<input type="image" src="{0}" name="submit" alt="Buy it Now" />""",
            self.get_image(),
        )