from paypal.standard.forms import PayPalPaymentsForm


class CustomPayPalPaymentsForm(PayPalPaymentsForm):

    def get_html_submit_element(self):
        return """<button type="submit">Procedi all&rsquo;acquisto</button>"""