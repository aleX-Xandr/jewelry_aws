from shop.models import Category, Material


def back(request):
    return request.META.get('HTTP_REFERER', '/')


def get_materials_for_slider():
    materials = Material.objects.filter()

    coulomb = Category.objects.filter(is_coulomb=True).first()
    for material in materials:
        products = coulomb.products.filter(materials__in=[material]).order_by('?')[:9]

        material.coulombs_1 = []
        material.coulombs_2 = []
        material.mob_coulombs_1 = []
        material.mob_coulombs_2 = []
        material.mob_coulombs_3 = []
        for i in range(len(products)):
            product = products[i]
            if i == 0:
                product.position = 'one'
                material.coulombs_1.append(product)
                material.mob_coulombs_1.append(product)
            elif i == 1:
                product.position = 'two'
                material.coulombs_1.append(product)
                material.mob_coulombs_1.append(product)
            elif i == 2:
                product.position = 'three'
                material.coulombs_1.append(product)
                material.mob_coulombs_1.append(product)
            elif i == 3:
                product.position = 'four'
                material.coulombs_1.append(product)
                material.mob_coulombs_2.append(product)
            elif i == 4:
                product.position = 'five'
                material.coulombs_2.append(product)
                material.mob_coulombs_2.append(product)
            elif i == 5:
                product.position = 'six'
                material.coulombs_2.append(product)
                material.mob_coulombs_2.append(product)
            elif i == 6:
                product.position = 'seven'
                material.coulombs_2.append(product)
                material.mob_coulombs_3.append(product)
            elif i == 7:
                product.position = 'eight'
                material.coulombs_2.append(product)
                material.mob_coulombs_3.append(product)
            elif i == 8:
                product.position = 'nine'
                material.coulombs_2.append(product)
                material.mob_coulombs_3.append(product)
    return materials
