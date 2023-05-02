def sum_of_multiples(limit, multiples):
    sum = 0
    products = set()
    for multiple in multiples:
        product = 0
        factor = 1
        while product < limit and multiple > 0:
            if product not in products:
                sum += product
                products.add(product)
            product = multiple * factor
            factor += 1
    return sum
