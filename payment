class Payment:
    # Process Payment
    def process_payment(self, policyholder):
        policyholder.payment_status = "Paid"
        print(f"Payment processed for {policyholder.name}. Payment status: {policyholder.payment_status}")  

    # Send payment reminder
    def send_payment_reminder(self, policyholder):
        if policyholder.payment_status != "Paid":
            print(f"Reminder: Payment is due for {policyholder.name}.")
        else:
            print(f"No reminder needed. Payment already made for {policyholder.name}.")

    # Apply payment penalty
    def apply_penalty(self, policyholder, penalty_amount):
        if policyholder.payment_status != "Paid":
            print(f"Penalty of ${penalty_amount} applied to {policyholder.name}.")
        else:
         print(f"No penalty applied. Payment already made for {policyholder.name}.")
    