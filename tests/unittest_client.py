import unittest
from unittest.mock import patch, MagicMock
from python.client import HiveClient
import requests


class TestHiveClient(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://localhost:3456"
        self.client = HiveClient(token="test_token")

    @patch("requests.post")
    def test_create_account(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "username": "testuser"}
        mock_post.return_value = mock_response

        # Act
        result = self.client.create_account("testuser")

        # Assert
        mock_post.assert_called_once_with(
            url=f"{self.base_url}/account",
            params={"username": "testuser"},
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"status": "success", "username": "testuser"})

    @patch("requests.patch")
    def test_update_username(self, mock_patch):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "success", "username": "newuser"}
        mock_patch.return_value = mock_response

        # Act
        result = self.client.update_username("newuser")

        # Assert
        mock_patch.assert_called_once_with(
            url=f"{self.base_url}/account",
            params={"username": "newuser"},
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"status": "success", "username": "newuser"})

    @patch("requests.get")
    def test_get_account_info(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"account": "info"}
        mock_get.return_value = mock_response

        # Act
        result = self.client.get_account_info()

        # Assert
        mock_get.assert_called_once_with(
            url=f"{self.base_url}/account",
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"account": "info"})

    @patch("requests.get")
    def test_get_models(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"model_id": 123, "model": "data"}
        mock_get.return_value = mock_response

        # Act
        result = self.client.get_models(model_id=123)

        # Assert
        mock_get.assert_called_once_with(
            url=f"{self.base_url}/model",
            params={"id": 123},
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"model_id": 123, "model": "data"})

    @patch("requests.post")
    def test_generate_api_key(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"api_key": "key123"}
        mock_post.return_value = mock_response

        # Act
        result = self.client.generate_api_key()

        # Assert
        mock_post.assert_called_once_with(
            url=f"{self.base_url}/apikey",
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"api_key": "key123"})

    @patch("requests.delete")
    def test_delete_api_key(self, mock_delete):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_delete.return_value = mock_response

        # Act
        result = self.client.delete_api_key()

        # Assert
        mock_delete.assert_called_once_with(
            url=f"{self.base_url}/apikey",
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"status": "deleted"})

    @patch("requests.get")
    def test_get_data_versions(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.json.return_value = {"version": "1.0"}
        mock_get.return_value = mock_response

        # Act
        result = self.client.get_data_versions(version="1.0")

        # Assert
        mock_get.assert_called_once_with(
            url=f"{self.base_url}/data_versions",
            params={"version": "1.0"},
            headers={"Authorization": "Bearer test_token"}
        )
        self.assertEqual(result, {"version": "1.0"})

    @patch("requests.post")
    def test_create_account_handles_404_error(self, mock_post):
        # Simulate a 404 error from the API
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"error": "Not Found"}
        mock_post.return_value = mock_response

        result = self.client.create_account("non_existing_user")

        self.assertEqual(result, {"error": "Not Found"})

    @patch("requests.post")
    def test_create_account_timeout(self, mock_post):
        # Simulate a timeout exception
        mock_post.side_effect = requests.exceptions.Timeout

        with self.assertRaises(requests.exceptions.Timeout):
            self.client.create_account("testuser")

if __name__ == '__main__':
    unittest.main()