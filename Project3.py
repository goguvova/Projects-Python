
##Sal's Shipping

def ground_shipping(weight):
  if weight<= 2:
    price_per_pound = 1.50
  elif weight <=6:
    price_per_pound = 3.00
  elif weight <=10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 +(weight * price_per_pound)

#print(ground_shipping(8.4))
premium_ground_shipping = 125
def drone_shipping(weight):
  if weight<= 2:
    price_per_pound = 4.50
  elif weight <=6:
    price_per_pound = 9.00
  elif weight <=10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return weight * price_per_pound
#print(drone_shipping(1.5))

def cheapest_method(weight):
  if ground_shipping(weight)<= premium_ground_shipping and ground_shipping(weight)<= drone_shipping(weight):
    return "You should ship using ground shipping it will cost "+ str(ground_shipping(weight))
  elif premium_ground_shipping<=ground_shipping(weight) and premium_ground_shipping<= drone_shipping(weight):
    return "You should ship using premium ground shipping it will cost "+ str(premium_ground_shipping)
  else :
   return "You should ship using drone shipping it will cost "+ str(drone_shipping(weight))
print(cheapest_method(42))
