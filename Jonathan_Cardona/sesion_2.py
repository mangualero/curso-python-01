#operadores aritmeticos
#suma
#resta
#multiplicacion
#division

store_name = "Bear company"
ice_cream = 5000
mango = 2000
corn = 1500

person = "Pepito"
total =int(ice_cream) + int(mango) + int(corn)
print(total)

new_total = total - corn
print(new_total)

total_products_to_party = 5 * mango + 20 * ice_cream + 16 * corn
print(total_products_to_party)
#descuento por compras mayores a 100000
discount = 10

total_products_discount = total_products_to_party *discount / 100
print(total_products_discount)
final_total = total_products_to_party - total_products_discount
print("final_total",final_total)
#activity

matematicas = 3
sociales = 4
artistica = 4.5
ingles = 5
español = 4.9

suma_final = matematicas + sociales + artistica + ingles + español
promedio = suma_final / 5
print(promedio)
#operadores logicos de comparacion
people = 2

place_to_party = people !=13
print(place_to_party)
#operadores logicos
