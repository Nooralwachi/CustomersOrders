class Product():
	def __init__(self,name,family,cost):
		self.name= name
		self.family= family
		self.cost=cost

class Order():
	def __init__(self,order_date,shipping_date,order_cost,shipping_cost,tax,products):
		self.order_date= order_date
		self.shipping_date= shipping_date
		self.shipping_cost=shipping_cost
		self.tax=tax 
		self.order_cost = order_cost
		self.products = products
	def getTotalCost(self):
		print(shipping_date + shipping_cost +tax)
	def getOrderStatus(self):
		if self.shipping_date:
			print("SHIPPED")
		elif self.order_date:
			print("PAID")
	def containsProduct(self, product_name):
		if self.product_name in self.products:
			print("Order " +slef.order_name + "contains in the order " + self.order_name)

class Customer():
	def __init__(self,firstname,lastname,shipping_add,billing_add, orders):
		self.firstname= firstname
		self.lastname = lastname
		self.shipping_add = shipping_add
		self.billing_add = billing_add
		self.orders = orders

	def print_customer(self):
		print("Customer: " + str(self.firstname) + ' ' + str(self.lastname))
	def getTotalOrderCost(self):
		final = 0
		for order in self.orders:
			total=0
			for item in order.products:
				total += item.cost
			total += order.shipping_cost+ order.tax
			final += total

		print("Total Orders:   $" +str(final))
	def getAverageOrderCost(self):
		count = 0
		final = 0
		for order in self.orders:
			total=0
			for item in order.products:
				count +=1
				total += item.cost
			total += order.shipping_cost+ order.tax
			final += total
		avg = final/count
		print("Average Orders: ${:.2f}".format(avg))

firstProduct= Product('Dream Phone','Dream',450.00)
secondProduct= Product('Dream Charger','Dream',20.00)
thirdProduct= Product('Star Phone','Star',225.00)

firstOrder = Order('03/30/2017','04/09/2017',0,13.94,1.05,[firstProduct, secondProduct])
secondOrder = Order('03/05/2017','03/15/2017',0,1.04,0.08,[thirdProduct])

firstCustomer = Customer("Adele","Dodson", "P.O. Box 871, 4183 Suspendisse Street","822-1897 At, St.",[firstOrder,secondOrder])
firstCustomer.print_customer()
firstCustomer.getAverageOrderCost()
firstCustomer.getTotalOrderCost()


