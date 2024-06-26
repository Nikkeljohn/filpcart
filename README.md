# MyHouse


Developer: <a href='https://github.com/Nikkeljohn' target='_blank'>Nikkel John</a>

Visit the [live site](https://myhome-1-30d4043086e4.herokuapp.com/)

This is my final project for the Full-Stack Software Development Course at Code Institute / University College Dublin

![screenshot](/images/home.png)

## Table of Contents

- [Introdution](#introdution)
    - [Business goals addressed with this site](#business-goals-addressed-with-this-site)
    - [Customer needs](#customer-needs)
- [UX](#ux)
    - [Business Goals](#business-goals-addressed-with-this-site)
    - [Ideal client](#ideal-client)
    - [Strategy](#strategy)
    - [Colour scheme](#colour-scheme)
    - [Typography](#typography)
    - [Images and Post Content](#images-and-post-content)
    - [Wireframes](#wireframes)
- [Agile Development Process](#agile-development-process)
    - [Strategy](#strategy)
    - [GitHub Projects](#github-projects)
    - [GitHub Issues](#github-issues)
    - [MosCow Prioritization](#moscow-prioritization)
- [User Stories](#user-stories)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to Implement in Future](#features-to-implement-in-future)
- [Database Design](#database-design)
- [Ecommerce Business Model](#ecommerce-business-model)
- [Search Engine Optimization (SEO) & Social Media Marketing](#search-engine-optimization-seo--social-media-marketing)
    - [Description and Keywords](#description-and-keywords)
    - [Sitemap](#sitemap)
    - [Robots](#robots)
    - [Social Media Marketing](#social-media-marketing)
    - [Newsletter Marketing](#newsletter-marketing)
- [Testing](#testing)
    - [HTML Code Validation](#html-code-validation)
    - [CSS Code Calidation](#css-code-validation)
    - [Manual Testing](#manual-testing)
        - [How to use Stripe test card](#how-to-use-stripe-test-card)
    - [Browser Testing](#browser-testing)
    - [Responsiveness](#responsiveness)
    - [Automatic Testing](#automatic-testing)
- [Configuration and Deployment](#configuration)
    - [ElephantSQL Database](#elephantsql-database)
    - [coludaniary AWS](#amazon-aws)
    - [Stripe API](#stripe-api)
    - [Gmail API](#gmail-api)
    - [Heroku Deployment](#heroku-deployment)
    - [Local Deployment](#local-deployment)
- [Technologies Used](#technologies-used)
    - [Programming Languages](#programming-languages)
    - [Hosting and Database](#hosting-and-database)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [Tools and Web Applications](#tools-and-web-applications)
    - [Code Validation](#code-validation)

- [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

## Introdution

The MyHome Store is a comprehensive Django website specialized created for an Irish local store sell Houses and household items online. There, users can search for products, buy them securely using Stripe Payments,  create a profile to leave product reviews, besides to keep an Order History. Also, the site a newsletter sign up and a blog section where users  can find content about house  and interact adding a comment or liking a post.

### Business goals addressed with this site
- Build brand awareness;
- Prensent the business value proposition with high-quality content;
- Catch customer's attention and offer a good experience on buying product.

### Customer needs
- Understand the purpose of the store;
- Buy a new product.
- Keep Order History.
- Signup to the newsletter for receiving news and 
discount cupoms.
- Interact with content about new arrivals and deals;

### Ideal client
- English speaking;
- Has interest about sell or buy houses hold items;
- Want to buy a household items.

Back to [top](#table-of-contents)

## UX

Thinking about the design was really simple, So I kept as simple and clean as possible.

The site flow is pretty basic, but efficient. The users can add items to their shopping bag and see the running total as they browse the site. This is a essential function to easy the buying process.

I've included an footer with a signup form where users can receive exclusive offers and discount codes by subscribing to the newsletter.

### Colour Scheme

I used [coolors.co](https://coolors.co/) to generate my colour palette.



### Typography

I used Google Fonts to select and import the font Poppins, including for main headers and the logo because it is modern but easily readable at the same time. [Lato](https://fonts.google.com/specimen/Lato) was used for all the text.



### Images and Post Content

All the  images on the site were gathered on [Amazon](https://www.amazon.com/ref=nav_logo) website.
The blog posts were oginaly published by []() magazine.

### Wireframes

I've used [Figma](https://www.figma.com/) to design my site wireframes.

| Page | Wireframe |
| --- | --- |
| Home | ![screenshot](/images/home.png) |
| Bag | ![screenshot](/images/bag.png) |
| profile detail | ![screenshot](/images/myprofile.png) |

Back to [top](#table-of-contents)

## Agile Development Process

### Strategy

 This project uses Agile Methodology. A planning session generated 34 Tasks through 19 User Stories and 8 Epics, each one with their acceptance criterias. 2 of then was not implemented and they are listed in the "Features to Implement in the Future" session. The development process was based on iterative incremental philosophy, adopting 1 week sprints with the following goals:

- <strong>Week 1</strong>: Basic structure and features running with boilerplate design and content.
- <strong>Week 2</strong>: CRUD functionalities of product section running with boilerplate design and content.
- <strong>Week 3</strong>: CRUD functionalities of blog section + Final version of the design and content + Messages.
- <strong>Week 4</strong>: Testing, final deploy and documentation.

### GitHub Projects

For this project, GitHub Projects was utilized as an Agile tool. While it's not a specialized tool, it can be customized with the appropriate tags and project creation/issue assignments to make it effective. User stories, issues, and milestone tasks were planned using it, then tracked on a weekly basis using the basic Kanban board.

![kanban-board] 

### GitHub Issues

GitHub Issues served as an another Agile tool for manage the issues throughout the development process.

![github-issues] 

### MoSCoW Prioritization

For prioritization, I used the MoSCow framework, adding labels to my tasks and user stories within the Github Issues.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: This will not be worked on

## User Stories

In order to enhance the efficiency of this project's development process, I mapped out 34 tasks through 29 user stories to build the website to a good standard. In addition, I splited these user stories into epics in order to take an agile approach towards their development.

View a full list of user stories [here](https://github.com/users/Nikkeljohn/projects/11).

### EPIC 1: General Site Functionality

- As a first-time visitor, I want to see what the site's purpose is so that I can decide whether or not to continue browsing it. `(MUST HAVE)`
- As a user I want to navigate the website's pages so that I can find the content I'm looking for. `(MUST HAVE)`
- As a site user I want to search for specific products in the website. `(SHOULD HAVE)`
- As a site user I want to contact the site owners so that I can request further information or lodge a complaint. `(WON'T HAVE)`

### EPIC 2: Products

- As a site user I want to see a list of all site products so that I can understand what the store's catalogue is. `(MUST HAVE)`
- As a site user I want to see the product price so that I can make a decision whether or not to purchase. `(MUST HAVE)`
- As a site user I want to view the product details page for more information about a particular product. `(MUST HAVE)`
- As a site user I want to sort products by category so that I can find related products of the same category. `(SHOULD HAVE)`
- As a site user I want to sort products by category so that I can find related products of the same category. `(SHOULD HAVE)`

- As a site user, I want to leave a review of a specific product so that I share my opinion and help other users who want to buy the same product. `(SHOULD HAVE)`

### EPIC 3: Ordering/Cart Management

- As a site user to add products to my shopping cart so that I can proceed to the checkout and purchase them. `(MUST HAVE)`
- As a site user I want to see the subtotal of the items in my basket to know what to expect at the checkout. `(MUST HAVE)`
- As a site user I want to checkout with a card payment so that I can place an order for the items in my shopping cart. `(MUST HAVE)`
- As a site user I want to receive an order confirmation email after I purchase so that I can have a record of what I've purchased in my email inbox. `(SHOULD HAVE)`

### EPIC 4: Site User Accounts

- As a site user, I want to login/logout of the site so that I can be an authenticated/not authenticated user. `(MUST HAVE)`
- As a site user I want to create an account on the site so that I can see a history of my purchases on my account and save my billing and shipping details. `(MUST HAVE)`
- As a registered user I want to edit my account details so that I can keep them up to date. `(SHOULD HAVE)`



### EPIC 5: Site Admin

- As a site admin I want to add new products from the front end so that I can easily manage the catalogue to the site. `(SHOULD HAVE)`
- As a site admin I want to edit existing products so that I can ensure that all product details are up to date. `(SHOULD HAVE)`
- As a site admin I want to delete products from the site so that I can remove any products that are no longer being on the catalogue. `(SHOULD HAVE)`

### EPIC 6: SEO & Marketing

- As a site admin I want to set appropriate meta tags on the site to enhance the chances of potential customers discovering my store via Google searches. `(MUST HAVE)`
- As a site user I want to sign up for the site's mailing list to receive offers and news. `(SHOULD HAVE)`
- As a site admin I want to send emails to people who signed up to the site's mailing list so that I can send out news and offers to them. `(WON'T HAVE)`
- As a site admin I want to be able to share the business on Facebook so that I can reach and market to a broader audience. `(SHOULD HAVE)`



Back to [top](#table-of-contents)

## Features

### Existing Features
| Feature | Description | Image |
| --- | --- | --- |
| Hero image | Presents a big image with a call to action for all products page. | |
| Footer | Divided in three section, presents a description of the MyHouse wich could be used to displays the physical address. A newsletter subscrition form and the social links |  |
| Search Bar | To find specific products, users can utilize the search bar in the navigation menu. The search term is compared to product names and descriptions to provide a list of products that match the user's search criteria. | 
| Filter by Price or Category | Through the topbar is possible to display the products ordered by price or category |  |
| All Products | This page displays all the available products |  |
| Product card | With a good image of the product, this card displays the name, category and price for a regular user. For the admin, there are two special links for editing or deleting the product. |  |
| Product | This page displays all the detailed informations about the products, besides the 'Add to Bag' buttom and a Reviews section where any logged user can leave a review. | !g) |
| Bag pop up | When the user add a product to the bag, this pop-up informs that the product was added with success to the bag, besides a summary of the bag and a yellow message about the free delivery offer |  |
| Shopping Bag Page | This page informs the items in the bag page for the user to double chech before the checkout. |  |
| Checkout Page | This page has the user fill in the delivery details and credit card info. For logged users, the name, email and delivery information can be saved to be pre-fill in the purchase. | 
| Order Confirmation Page | Once the order is done, the user will be directed to a confirmation page that informs them that an email containing the order confirmation has been sent to their provided email address. | 
| Profile page | This page stores the user's default delivery information and the order history. Each order number has a link to its order confirmation page | |
| Profile Page | This page stores the user's default delivery information and the order history. Each order number has a link to its order confirmation page | |
| Error Page | If the user ends up in a broken link or a page the doesn't exist, a error page is displayed informing that the page they are looking for isn't available. | |
| Add Product | As an admin user, there is the possibility of add a new product to the site from the My Account >>> Product Management dropdown menu in the navbar |  |
| Review Product | As a logged user, you can leave a product review and help other users who are interested in that produc too. |  |
| Blog page | Displays a list of articles about music and products that are sold on the site. |  |
| Blog post | Displays an article and the comment setion. |  |
|Contact form| Allows the user to send a message to the Site Admin. | |
	


### Features to Implement in Future


- Delete account: Allows the user to delete their account
- Wishlist: Allow the user to add a product to their wishlist so that they can receive news and offers about that product.

Back to [top](#table-of-contents)


## Database Design

Before starting code and create models, I built a Relationship Diagrams (ERD) with [Lucidchard](https://lucid.app/) to better visualize the database architecture.

![database-driagram](/images/database.png) 

### Models
The following models were created for MyHouse.

- Category
```python
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
```

- Product
```python
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
```


- Profile
```python
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
   user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

```

- Order
```python
class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100  # noqa
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number
        if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

```

- Order Line Item
```python
class OrderLineItem(models.Model):

    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
```

- Post
```python
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
```


- Contact
```python
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Table"
```

Back to [top](#table-of-contents)


## Ecommerce Business Model

The MyHouse is dedicated to selling products to individual customers through a simple Business to Customer model (B2B). The site is still in its early stages; however, it already offers a newsletter and social media marketing links to promote the business. By leveraging social media platforms like Facebook, we can build a community of users around the site, leading to an increase in visitor numbers and consequently more purchases.

The newsletter is an effective tool for us to communicate regular updates to our users. It is an excellent way to share information about special offers, new product updates, changes in business hours, notifications of events, and more. Our goal is to ensure that our users are always up-to-date and informed.

Back to [top](#table-of-contents)




### Robots

The [robots.txt](robots.txt) file is at the root-level of this project.
Inside, I've included the default settings as follows:

```
User-agent: *
Disallow: /profiles/
Disallow: /bag/

```

### Social Media Marketing

Building a robust social network with active participation and connecting it to your business website can lead to increased sales.

I've created a Facebook business account wich can be acessed in the [following url](https://www.facebook.com/profile.php?id=61550252952582) by the time when this project was sent to Code Institute's validation, but sometimes Facebook exclude 'fake business pages' like these:

![facebook-page](/images/fb.png)

### Newsletter Marketing

## To do

In the website footer there is a newsletter sign-up form, to allow users to supply their
email address if they are interested in receiving news.

![newsletter]

Back to [top](#table-of-contents)

## Testing


### Python Code Validation
![screenshot](/images/python/Screenshot%202024-05-02%20at%2012.36.21.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2012.36.21.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2012.36.21.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2013.25.51.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2013.42.55.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2013.46.09.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2013.51.21.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2014.19.40.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2014.33.51.png)
![screenshot](/images/python/Screenshot%202024-05-02%20at%2014.20.35.png)


### HTML Code Validation

The W3C Markup Validation Service was used to validate the HTML of the website. All Django template tags were manually removed with the HTML code copied and inserted to the base template.
🛑🛑 TO-DO
<details>
<summary><strong>base.html</strong> </summary>

![base.html](/images/html/home.png)
</details>

<details>
<summary> <strong>add-product.html</strong></summary>

![add_product.html](/images/html/3.png)

</details>

<details>
<summary> <strong>bag.html</strong></summary>

![bag.html](/images/html/Screenshot%202024-05-03%20at%2020.03.59.png)

</details>



<details>
<summary> <strong>checkout_success.html</strong></summary>

![checkout_success.html](/images/html/3.png)

</details>

<details>
<summary> <strong>checkout.html</strong></summary>

![checkout.html](/images/html/3.png)

</details>

<details>
<summary> <strong>edit_product.html</strong></summary>

![edit_product.html](/images/html/3.png)

</details>

<details>
<summary> <strong>post_detail.html</strong></summary>

![post-detail.html](/images/html/3.png)

</details>

<details>
<summary> <strong>products.html</strong></summary>

![products.html](/images/html/3.png)

</details>

<details>
<summary> <strong>blog.html</strong></summary>

![blog.html](/images/html/3.png)
![blog_detail.html](/images/html/)

</details>

<details>
<summary> <strong>profile.html</strong></summary>

![profile.html](/images/blog2.png)
Erorrs are 3rd party side 
and 3 internal warrings like every html 

</details>


### CSS Code Validation
CSS file validation results generated with W3C Validation Service


<summary> <strong>base.css</strong></summary>

![screenshot](/images/python/csscheck.png)




### Manual testing

| Test Label | Test Action | Expected Outcome | Test Outcome |
| --- | --- | --- | --- |
| Site loading | Navigate to the “Homepage”, “Login”, “Register”, “Add a product”, “Logout” and “All Products”. | All the pages and elements are loaded according. | PASS  |
| Add a product in the bag | On the product detail page, click the "Add to bag" button”. | The product is added to the bag and can be found in the bag page. | PASS |
| Checkout | On the checkout page, fill the form with user details, delivery details and the Stripe Test Credit info. | The checkout in done, a order confirmation page is displayed and a email confirmation is sent. | PASS |
| Add a product | On the navbar, click the “Product Management” option, fill out the form and hit the “Submit” button. | A success message must be displayed and the product must be listed on the “All Products” page. | PASS |
| Edit a product | On the products page, click the “Edit” button, change some info on the form and hit the “Submit” button. | A success message must be displayed and the product info must be updated. | PASS |
| Delete a Product | On the products page, click the “Delete”. | The product must be deleted. | PASS |

#### How to use Stripe test card
When testing interactively, use a card number, such as 4242 4242 4242 4242. Enter the card number in the Dashboard or in any payment form.

- Use a valid future date, such as 12/34.
- Use any three-digit CVC (four digits for American Express cards).
- Use any value you like for other form fields.
See more on [Stripe site](https://stripe.com/docs/testing#testing-interactively)
![Stripe Test Card](/documentation/stripe-test-cardjpg.jpg)

### Browser Testing
I have tested this application works on the following installed browsers, using a Dell laptop on Windows OS:

- Google Chrome Version 


### Responsiveness
I used Chrome developer tool to check the responsiveness on different screen sizes:
- 375px (Mobile)
- 728px (Tablet)
- 1024px (laptop)



## Configuration and Deployment

The live deployed application can be found deployed on https://myhome-1-30d4043086e4.herokuapp.com/

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:
- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: 🛑 NAME 🛑).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.


### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- Add your deployed site link.
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or guitar-store
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_API_KEY` | user's own value |
| `CLOUDINARY_API_SECRET` | user's own value |
| `DATABASE_URL` | user's own value |
| `EMAIL_HOST_PASS` | user's own value |
| `EMAIL_HOST_USER` | user's own value |
| `SECRET_KEY` | user's own value |
| `STRIPE_PUBLIC_KEY` | user's own value |
| `STRIPE_SECRET_KEY` | user's own value |
| `STRIPE_WH_SECRET` | user's own value |


Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault["CLOUDINARY_API_KEY", "user's own value"] 
os.environ.setdefault["CLOUDINARY_API_SECRET" ,"user's own value"]
os.environ.setdefault["CLOUDINARY_CLOUD_NAME", "user's own value"]
os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("EMAIL_HOST_PASS", "user's own value")
os.environ.setdefault("EMAIL_HOST_USER", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "user's own value")
os.environ.setdefault("STRIPE_SECRET_KEY", "user's own value")
os.environ.setdefault("STRIPE_WH_SECRET", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:
- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:
- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Nikkeljohn/filpcart) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Nikkeljohn/filpcart`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)]()

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Nikkeljohn)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

Back to [top](#table-of-contents)

## Technologies Used
### Programming Languages

- [Python](https://www.python.org) used as the back-end programming language.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.

### Hosting and Database
- [Cloudinary](https://console.cloudinary.com) used for online static file storage.- 
- [GitHub](https://github.com) used for secure online code storage.

### Frameworks and Libraries
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [Bootstrap 4](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [PostgreSQL](https://www.postgresql.org) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.

### Tools and Web Applications
- [Stripe](https://stripe.com) used for online secure payments of ecommerce products/services.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [Figma](https://figma.com): used for creating wireframes.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Lucidchart](https://www.lucidchart.com/) used to design the database diagram.

### Code Validation
- [JSHint](https://jshint.com/): used for Javascript code validation.
- [PEP8](https://peps.python.org/pep-0008/): used for Python code validation.
- [Lighthouse](https://developer.chrome.com/docs/devtools/) Testing site performance on desktop and mobile devices.
- [W3C HTML](https://validator.w3.org/): used for HTML code validation.
- [W3C CSS](https://jigsaw.w3.org/css-validator/): used for CSS code validation.

Back to [top](#table-of-contents)

## Credits

### Content

- All the producrt  images were taken from google 

- README Documenting was inspired by [Retro Reboot](https://github.com/adamgilroy22/retro-reboot/) and [FreshCats](https://github.com/RickofManc/fresh-casts)

### Acknowledgements

- I would like to thank my wife (shintu), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my Code Institute's mentor (Dasiy and )&(Juliia_Konn), and the tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the Code Institute Slack community for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank the my friends and family.

Back to [top](#table-of-contents)