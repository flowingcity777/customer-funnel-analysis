import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visit_cart = pd.merge(
  visits,
  cart,
  how='left'
)

print(f"Total visitors: {len(visit_cart)}")

null_cart_time = visit_cart['cart_time'].isnull().sum()

print(f"Visitors without a cart: {null_cart_time}")

percent_cart_visit_null = (
    visit_cart.cart_time.isnull().sum()
    /
    len(visit_cart)
) * 100

print(percent_cart_visit_null)

cart_checkout = pd.merge(
  cart,
  checkout,
  how='left'
)

cart_checkout.info()

null_checkout_time = cart_checkout['checkout_time'].isnull().sum()

print(null_checkout_time)

percent_cart_checkout_null = (
  cart_checkout.checkout_time.isnull().sum()
   /
  len(cart_checkout)
) * 100

print(percent_cart_checkout_null)

all_data = (
    visits
    .merge(cart, how='left')
    .merge(checkout, how='left')
    .merge(purchase, how='left')
)

checkout_not_purchase_percent = (len(all_data[all_data.checkout_time.notnull() & all_data.purchase_time.isnull()]) / float(len(all_data[all_data.checkout_time.notnull()]))) * 100

visit_to_cart_percent = (len(all_data[all_data.visit_time.notnull() & all_data.cart_time.isnull()]) / float(len(all_data[all_data.visit_time.notnull()]))) * 100

cart_to_checkout_percent = (len(all_data[all_data.cart_time.notnull() & all_data.checkout_time.isnull()]) / float(len(all_data[all_data.cart_time.notnull()]))) * 100

print(f"Visitors without cart: {visit_to_cart_percent:.2f}%")
print(f"Cart without checkout: {cart_to_checkout_percent:.2f}%")
print(f"Checkout without purchase: {checkout_not_purchase_percent:.2f}%")

# Task 9: Funnel Analysis
# Note: Using `all_data` yields slightly different percentages than individual merged steps 
# due to row duplication across repeated left merges. However, both methods identify 
# "Visit -> Cart" as the weakest step by a wide margin (~69.6% vs 16.9% and 16.9%).

all_data['difference'] = all_data['purchase_time'] - all_data['visit_time']

print(all_data['difference'].mean())
