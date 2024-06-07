from order.models import Order


class OrderService:
    def get_order(self, request):
        if request.user.is_authenticated:
            order, created = Order.objects.get_or_create(user=request.user)
        else:
            session_key = request.session.session_key
            if not session_key:
                request.session.create()
                session_key = request.session.session_key
            order, created = Order.objects.get_or_create(session_key=session_key)
        return order


order_service = OrderService()
