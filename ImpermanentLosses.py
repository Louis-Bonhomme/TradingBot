# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:13:10 2021

@author: etx01msp
"""

prix_initiale_coin1 = 40
prix_initiale_coin2 = 50000
    
nombre_coin1_acheté = 440

print("You buyed " + str(nombre_coin1_acheté) + " coin1 for " + str(prix_initiale_coin1*nombre_coin1_acheté) + " $")


nombre_coin1_pooled = nombre_coin1_acheté/2
nombre_coin2_pooled = nombre_coin1_pooled*prix_initiale_coin1/prix_initiale_coin2

print("You pooled " + str(nombre_coin1_pooled) + " coin1 for " + str(prix_initiale_coin1*nombre_coin1_pooled))

print("You pooled " + str(nombre_coin2_pooled) + " coin2 for " + str(prix_initiale_coin2*nombre_coin2_pooled))

my_pool_initial_value = prix_initiale_coin2*nombre_coin2_pooled + prix_initiale_coin1*nombre_coin1_pooled

print("Your INITIAL total liquidity value is : " + str(my_pool_initial_value) )
  
#nombre_coin2_deposited 
#
prix_coin1_dollar = 35

prix_coin2_dollar = 60000
    

price_ratio = (prix_coin1_dollar / prix_initiale_coin1 ) / (prix_coin2_dollar / prix_initiale_coin2 )

print("price ratio : " + str(price_ratio))

impermanentLosses = 2*((price_ratio**0.5)/(1+price_ratio)) - 1 
impermanentLossesPourcentage = impermanentLosses *100

print("Impermanent Losses : " +str(impermanentLosses))

value_if_hold = nombre_coin1_pooled*prix_coin1_dollar   + nombre_coin2_pooled*prix_coin2_dollar



print("Your total value if HODL is : " + str(value_if_hold))

my_pool_value = value_if_hold - abs(impermanentLosses) * value_if_hold

print("Your total liquidity value NOW is : " + str(my_pool_value))
  
#How much coin now ?



nombre_coin2 = my_pool_value/(2*prix_coin2_dollar)

nombre_coin1 = my_pool_value/(2*prix_coin1_dollar)

print("Your liquidity of coin 1 is NOW : " + str(nombre_coin1))

print("Your liquidity of coin 2 is NOW : " + str(nombre_coin2))

#impermanentLosses = my_pool_value/value_if_hold

pangolin_farmed = 1200
prix_pangolin = 0.21*prix_coin1_dollar

print("Your pangolin farming earned you : " + str(pangolin_farmed*prix_pangolin))