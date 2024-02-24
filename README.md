E commerce Project documentation¶
Documentation for the project
1)<h2>Registration</h2>
To register any Costumer u have to send the post request on below Endpoint with the value  (username ,password ,email ,phone ,add)
Endpoint:- http://127.0.0.1:8000/account/register
To register a Costumer
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/08878506-b782-4c45-858c-e0395e6410bc)
2)<h2>Login</h2>
For Login U have to pass the username and password in response of which will u get the Access Token
EndPoints:-http://127.0.0.1:8000/api/token/
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/756d4f4f-76db-4228-9a46-14f8f1fe8ff5)
Pass the Access Token as the Bearer for Authentication
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/42c4b112-25e4-49f1-909a-c0097f1d95f5)
EndPoints:-http://127.0.0.1:8000/login/
For a simple log in(But will not keep the session on)
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/4f73661c-1239-437c-98f3-1c3f1bf66200)
3)<h2>Logout</h2>
For logging out just hit a get request on below endpoint 
EndPoints:-http://127.0.0.1:8000/logout/ 
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/2617d9f5-f2ba-414c-b1cf-52e2156247d1)
4)<h2>To see All the products Hit a get request a below Endpoint</h2>
Endpoint:-http://127.0.0.1:8000/
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/5cca7823-0fa4-482a-a4ff-fd789aa437c1)
5)<h2>To See The detail View of a product</h2>
Hit Get request on the Below endpoint
Endpoint:-http://127.0.0.1:8000/<int:pk>
In “pk” u have to pass the id of the product
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/f63148b9-d30a-4255-8954-328b2a234845)
6)<h2>Searching</h2>
For searching  a item u can use the below Endpoint where the “str” is the keyword to search
Endpoint:-http://127.0.0.1:8000/search/<str:query>/
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/c2a9a445-e861-4cf3-bd8c-21742ee08cec)
7)<h2>Add to cart</h2>
Endpoint :-http://127.0.0.1:8000/cart/addData<int:pk>
Case1:-<h3>If user is not Authenticated</h3>
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/c9b92b34-6e5e-460a-9e28-e99a02ec8d9f)

Case2:-<h3>If user is Authenticated u can see the list of all cart of current login user</h3>
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/0f3c7a91-6e37-4bcf-b4c8-7b47f44d3930)
8)<h2>Session based request</h2>:- To keep session we have use the JWT As in above example of seeing the Cart
9)<h2>Remove</h2>:- To delete the cart item only admin and cart owner can perform this action
Endpoint -http://127.0.0.1:8000/cart/DeleteData/<int:pk>/
The “pk” is the id of the cart
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/10a91b7c-db4a-4a08-85bf-573ac55a9d95)
http://127.0.0.1:8000/cart/ to see the list of Current user All Carts
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/40e662f2-e2e9-440f-bbda-56a0c58a66f9)
9)<h2>Place Order</h2>:-To place a order user must be Authenticated and hit the below endpoint 
Endpoint:- http://127.0.0.1:8000/order/addData/<int:pk>
The “pk” is the product id that user want to book
<h3>Case 1</h3>:- If the Stock of the item has finished the order will not be place
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/f6fc1128-4bc0-4d3e-bdc2-f54e0629e35e)
<h3>Case 2</h3>:- If the Stock >0 and user is authenticated can place the order successfully
On placing a order the stock of product will be decrement by one
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/43eefd58-af79-40c3-a319-f32f004393eb)

http://127.0.0.1:8000/order/ to see the list of All the order of Log in user
![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/cfd5f862-8194-4b9a-90ad-34b80c050789)

Update the stock quantity of products when an order is placed.
<h2>Dashboard</h2>
http://127.0.0.1:8000/account/ dashboard
To see the dashboard of the logged in user In this user can see the list of all his Item in cart and items in the order list

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/8b06dfa7-a336-4064-9456-59d1f1f949fc)

Order history:- here user can see the list of all his order if user is authenticated
http://127.0.0.1:8000/order/

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/d2c18046-8312-447d-932c-ee6e17fdce18)

10)<h2>Admin</h2>
To see the Admin panel and using the CRUD functionality u can go to below endpoint
http://127.0.0.1:8000/admin/
If user is not admin he can’t log in image 1

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/e466624b-d57a-4ef0-80c2-209af2087008)

If user is admin he will go to admin section which will be like as below in image 

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/c1714276-8ddc-426c-b651-7723915b6588)

Example of the CRUD in Admin panel

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/69358f82-83d4-420b-92a4-be3542fb7d4a)

If user is not admin Not Authorize to see the admin view

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/ef04febf-649a-4981-ae05-92ecc2af08da)

If the user is admin
Will be Authorized to see the Admin view
Cart admin View:- The Admin Will be Able to see the All Cart Item
Endpoint:- http://127.0.0.1:8000/cart/admin/

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/8b4334b0-eb65-4912-ab28-8727e5b2cc52)

Order admin View:- The Admin Will be Able to see the All Order Item
Endpoint¬:-http://127.0.0.1:8000/order/admin/ 

![image](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/c878160c-a55a-42b8-a62c-4b52bc740f86)

<h2>Paytm</h2>
For the paytm unhave to hit the endpoint
http://127.0.0.1:8000/paytm/pay/
![paytm](https://github.com/avinash1410-cyber/E-commerce/assets/74523129/ef2e4048-ca42-4212-9c95-1918ae6af333)
Which will generate the checksumhash
which can be use for automatically call the
http://127.0.0.1:8000/paytm/response/
and pass the checksumhash for further payment
