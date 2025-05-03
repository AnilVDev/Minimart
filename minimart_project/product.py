# # ---- product.py ----

# def get_all():
#     from model_layer import Product
#     return Product.objects.all()

# def get_prod_by_id(id):
#     from model_layer import Product
#     prod = Product.objects.get(pk=id)
#     return {
#         'title': prod.name,
#         'cost': prod.cost,
#         'stock': prod.in_stock,
#         'category': 'none'  # hardcoded
#     }

# def reduce_stock(p_id, q):
#     from model_layer import Product
#     prod = Product.objects.get(id=p_id)
#     prod.in_stock = prod.in_stock - q
#     prod.save()
#     return True

# # Unused helper function
# def print_product():
#     print('This is product file')
