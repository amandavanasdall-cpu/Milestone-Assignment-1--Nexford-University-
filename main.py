# Import classes from other files
from policyholder import Policyholder
from product import Product
from payment import Payment

#------------
# Create Insurance Products
#-------------

pet_insurance = Product(101, "Pet Insurance", 300.00)
home_insurance = Product(102, "Home Insurance", 500.00)

# Create products
pet_insurance.create_product()
home_insurance.create_product()

#--------------
#Create policyholders
#--------------

policyholder1 = Policyholder(1, "Abby Doe")
policyholder2 = Policyholder(2, "Avery Smith")

#----------
# Assign Products to Policyholders
#----------

policyholder1.assign_product(pet_insurance)
policyholder2.assign_product(home_insurance)

#-----------
# Process Payments
#-----------

payment = Payment()

payment.process_payment(policyholder1)
payment.process_payment(policyholder2)

#-----------
# Payment reminder and penalties
#-----------

payment.send_payment_reminder(policyholder1)
payment.apply_penalty(policyholder2, 70)

#------------
# Suspend and Reactivate Policyholder
#------------

policyholder2.suspend_policyholder()
policyholder2.reactivate_policyholder()

#---------
# Display Account Details
#---------

print("\nPolicyholder Information:")

policyholder1.display_account_details()
policyholder2.display_account_details()


