
# from django.http import JsonResponse
# from .model_layer import Customer, Order, OrderItem, Product

# def show_customer_orders(request, cust_id):
#     c = Customer.objects.get(id=cust_id)
#     orders = Order.objects.filter(customer=c)
#     result = []
#     for o in orders:
#         items = OrderItem.objects.filter(order=o)
#         res = []
#         for i in items:
#             p = Product.objects.get(id=i.product.id)
#             res.append({'name': p.name, 'cost': p.cost, 'qty': i.qty})
#         result.append({'id': o.id, 'time': o.date, 'items': res})
#     return JsonResponse({'result': result})