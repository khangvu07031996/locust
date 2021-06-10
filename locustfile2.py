from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(3, 10)
    host = 'https://api.sungame.vn'
    @task
    def on_start(self):
        self.client.get("/data/banners", name='GET data/banners')

