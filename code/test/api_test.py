import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL= "http://127.0.0.1:8080"
    def test_get_recommendations(self):
        url = f"{self.BASE_URL}/get-recommendations/"
        payload = {"cust_id": "cust_001"}
        response = requests.post(url,json=payload)
        self.assertEqual(response.status_code,200,"API should return status code 200")

        # Assert the response format
        response_json = response.json()
        self.assertIn("recommendations", response_json, "Response should contain 'recommendations' key")
    def test_invalid_cust_id(self):
        # Test case for an invalid customer ID
        url = f"{self.BASE_URL}/get-recommendations/"
        payload = {"cust_id": "invalid_cust_id"}
        
        # Send a POST request to the API
        response = requests.post(url, json=payload)
        
        # Assert the response status code
        self.assertEqual(response.status_code, 404, "API should return status code 404 for invalid customer ID")

if __name__ == "__main__":
    unittest.main()