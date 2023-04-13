First I have created a User app for login and logout.
I have used django.contrib.auth.forms for UserRegistration
In User App There are three templates Registration, login and logout.
All forms are created by using crispy forms.
I have also added LOGIN_REDIRECT_URL to redirt after successfull login
Then created an another app named stock to show different stocks
Created fields used by stock in models.py
Map the url for stock/detail, to list all the stock entries
I have used login_required decorater to restrict the logged in users to access stock listing.
I have also added New Stock creation page using StockCreateView
Also showed Stock Detail View by using StockDetailView.
Added Load more button in stock detail list view.
Load more button will only be visible when stock entries exceed 5.
After click on Load more button and ajax request will get the other 5 entries from db and will append them to existing div.

