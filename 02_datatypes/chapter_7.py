masala_spices = ("cardamom", "cloves", "cinammon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spice: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardmom_ratio = 2, 1
print(f"Spice ratio G:{ginger_ratio} and C:{cardmom_ratio}")

# Flip the ratios
ginger_ratio, cardmom_ratio = cardmom_ratio, ginger_ratio
print(f"Spice ratio G:{ginger_ratio} and C:{cardmom_ratio}")

# Membership Test

print(f"is ginger in masala spices ? {'ginger' in masala_spices}")
print(f"is cinammon in masala spices ? {'cinammon' in masala_spices}")