from locust import HttpUser, task, between,TaskSet


class CreateSaleOrders(TaskSet):
    @task
    def create_sale_order(self):
        data = {
            'seller': 4,
            'phone': '09029813840',
            'amount': 5
        }

        self.client.post('sell/',json=data)


class WebsiteUser(HttpUser):
    tasks=[CreateSaleOrders]
    wait_time = between(1,5)
   