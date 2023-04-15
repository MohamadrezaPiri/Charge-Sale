from locust import HttpUser, task, between,TaskSet


class CreateSaleOrders(TaskSet):
    @task
    def create_sale_order(self):
        data = {
            'seller': 3,
            'phone': '09029813840',
            'amount': 5
        }

        self.client.post('sell/',json=data)




   