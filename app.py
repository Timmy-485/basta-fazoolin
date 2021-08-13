class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return ("{} menu is available from {} to {}").format(self.name, self.start_time, self.end_time)

  def calculate_bill(self,  purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total


brunch_menu = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_menu, 1100, 1600)


early_bird_menu = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("Early Bird", early_bird_menu, 1500, 1800)


dinner_menu = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", dinner_menu, 1700, 2300)



kids_menu = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
kids = Menu("Kids", kids_menu, 1100, 2100)



brunch_total = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
print(brunch_total)

early_bird_bill = early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print(early_bird_bill)


class Business:
  def __init__(self, name, franchises):
    self.name =name
    self.franchises = franchises



class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    menu_list = []
    for x in self.menus:
      if time >= x.start_time and time <= x.end_time:
        menu_list.append(x)
    return menu_list

all_menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment_store = Franchise("12 East Mulberry Street", all_menus)

print(flagship_store)
print(flagship_store.available_menus(1200))



basta_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment_store])

arepa_stuff = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa_menu = Menu("Take a’ Arepa", arepa_stuff, 1000, 2000)
arepa_franchise = Franchise("189 Fitzgerald Avenue", [arepa_menu])

arepa_business = Business("Take a' Arepa", [arepa_franchise])
print(arepa_business.franchises[0])

