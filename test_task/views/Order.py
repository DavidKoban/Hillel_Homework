from django.views.generic import TemplateView
from test_task.models import Order


class Order_View(TemplateView):
    template_name = 'order.html'

    def get_context_data(self, **kwargs):
        return {
            'orders': [
                {
                    'id': order.table_id,
                    'order_number': order.order_number,
                    'cost_usd': order.cost_usd,
                    'cost_rub': order.cost_uah,
                    'delivery_time': order.delivery_time,
                }
                for order in Order.objects.all().order_by('table_id')
            ],
        }