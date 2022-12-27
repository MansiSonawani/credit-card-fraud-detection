# credit-card-fraud-detection

Factors indicating a fraud in transactions

1. Large orders
Ex: If someone orders a quantity that was way over the usual, make sure to follow up about that order. For example, say you’re an online clothing store, and your average buyer buys 3 shirts but an order comes through for 54. It’s best to have your system set up to flag this transaction and then reach out directly to the customer.

2. Same product, multiple skews
Ex: If someone orders the same shirt in 6 sizes and all different colors, that’s a weird order — especially if you aren’t a bulk t-shirt organization.

3. Big-ticket items
Ex: You only offer one $2,000 item and three orders come through from an out-of-state card.

4. Large orders, multiple payment cards
Ex: Someone puts in a high quantity order back-to-back with the same name and email but 3 separate credit cards.

5. Same address, different cards
Ex: Someone uses 3 cards across 5 orders with the same billing and shipping address. This is a common fraud tactic in electronic equipment retailers.

6. One card, multiple shipping addresses
Ex: Someone buys a bunch of consecutive items to different addresses — especially if they are in different states and are to personal addresses instead of business addresses.

7. Same IP address, different cards
Ex: You’re a B2C and the same computer is ordering a series of products from you with different cards to the same address.

8. Multiple orders, similar card numbers
Ex: An order comes through where the first 12 digits are the same and the last four are switched just slightly.

9. Declined purchase followed by small ones
Ex: Someone tried to order a high price item and was caught by the system, so they are trying with a bunch of small items.

10. Incorrect expiration dates
Ex: An order has the number and security code right but repeatedly messes up the expiration date. Make sure your system flags this after 5 attempts or so.

11. Can’t provide personal info by phone
Ex: If someone calls about placing or following up on an order and can’t confirm any of their billing information apart from the credit card, you should probably dig a bit deeper.

12. Spelling errors or all caps
Ex: If the shipping address comes through as LAS ANGILIES, it’s probably worth looking into and giving the original owner a call.

13. Rush shipping on large orders
Ex: Use your judgment here based on your business, but if you aren’t a B2B plugged into some essential supply chain, exercise caution when someone wants something big as soon as humanly possible.

14. Repeat inquiries about shipping/delivery dates
Ex: Someone is extremely persistent about when and where something will be delivered (earlier than what would be expected). Make sure to ask some more confirmation questions when this occurs.

15. International shipping
Ex: Someone asks for a special request on international shipping. Review these often — especially if they are rare and high ticket.

16. Unaffected by costs
Ex: A customer service operator says they can add shipping but it’s a large sum and the customer doesn’t even hesitate.

17. Disinterest in returns
Ex: A customer says they don’t need to hear or care about returns on a very large purchase.

18. Uses deaf system relay to place orders
Ex: Sometimes people use systems designed for deaf people (third-party services, etc.) to place orders. Keep an eye on these style orders, as they are often an avenue for fraudsters to order without having to interact with a company.

19. Takes a while to sign the sales draft
Ex: Someone flies through every bit of the process but hesitates at the sales draft.

20. Suspicious credit cards
Ex: Credits cards having varying fonts and character sizes, no mag stripe or chip, or a weird-looking signature section.

21. No shopping history
Ex: If someone places a large new order without any shopping history associated with that card and person (especially if you are a large retailer), be careful.

22. Fake email addresses
Ex: Everything is correct except the email address is something like GTI#)!enw@gmail.com.



The major factor that I have taken into consideration in this project is the transaction pattern




TO RUN LOCALLY IN VIRTUAL ENV
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1


