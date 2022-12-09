from Order.models import CartModel,Cart_item
def extras(request):
        if request.user.is_authenticated:
                basket_items = CartModel.objects.filter(cart_items__user_id = request.user)
                products = Cart_item.objects.filter(user_id = request.user)
                grand_total = 0
                for product in products:
                        grand_total += product.total
                return {'basket_items': basket_items,
                'total_price':grand_total}

        else:
                basket_items = ''
                return {'basket_items': basket_items}