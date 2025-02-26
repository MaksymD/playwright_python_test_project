import pytest
import httpx
import allure
import json
import os
from fixtures.conftest import LOGGER


@allure.step("Load expected JSON from file: {file_path}")
def load_expected_json(file_path: str):
    """Helper function to load the expected JSON response from a file."""
    LOGGER.info(f"Loading expected JSON from file: {file_path}")
    assert os.path.exists(file_path), f"Expected JSON file not found at {file_path}"
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@allure.step("Asserting that the status code is 200")
def assert_status_code_is_200(response):
    """Helper function to assert the status code and provide a detailed error message."""
    LOGGER.info(f"Asserting status code: {response.status_code}")
    assert response.status_code == 200, (
        f"Expected status code 200, but got {response.status_code}. "
        f"Response Body: {response.text}"
    )


@allure.step("Asserting that the status code is 201")
def assert_status_code_is_201(response):
    """Helper function to assert the status code and provide a detailed error message."""
    LOGGER.info(f"Asserting status code: {response.status_code}")
    assert response.status_code == 201, (
        f"Expected status code 201, but got {response.status_code}. "
        f"Response Body: {response.text}"
    )


@allure.step("Parse and assert response JSON")
def parse_and_assert_response_json(response):
    """Parse response and assert it is a valid JSON object."""
    LOGGER.info("Parsing response JSON")
    try:
        actual_response = response.json()
        assert isinstance(actual_response, dict), "Expected a JSON object"
        return actual_response
    except ValueError as e:
        LOGGER.error(f"Failed to parse JSON: {e}")
        assert False, f"Response is not a valid JSON: {e}"


@allure.step("Attach actual and expected JSON to Allure")
def attach_responses_to_allure(actual_response, expected_response):
    """Attach actual and expected JSON responses to Allure for comparison."""
    LOGGER.info("Attaching responses to Allure")
    allure.attach(json.dumps(actual_response, indent=4), name="Actual Response Body",
                  attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(expected_response, indent=4), name="Expected Response Body",
                  attachment_type=allure.attachment_type.JSON)


@allure.parent_suite("API tests")
@allure.suite("User")
@allure.tag("API Test")
@allure.title("Test Case 1: POST Create/Register User Account")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    API URL: https://automationexercise.com/api/createAccount
    Request Method: POST
    Request Parameters: name, email, password, title, birth_date, birth_month, birth_year, 
                        firstname, lastname, company, address1, address2, country, zipcode, 
                        state, city, mobile_number
    Verify: 
    1. Response Code: 200
    2. Response Body: User created!""")
@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_post_create_user():
    api_url = "https://automationexercise.com/api/createAccount"
    request_data = {
        "name": "Max Musterman",
        "email": "max.mustermann@example.com",
        "password": "password",
        "title": "Mr",
        "birth_date": "1",
        "birth_month": "1",
        "birth_year": "1980",
        "firstname": "Max",
        "lastname": "Musterman",
        "company": "MusterCompany",
        "address1": "Musterstr. 123",
        "address2": "Musterstr. 123",
        "country": "Canada",
        "zipcode": "12345",
        "state": "Toronto",
        "city": "Musterstadt",
        "mobile_number": "+00 171 1234567"
    }
    LOGGER.info(f"Testing API: {api_url}")

    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, data=request_data)

        # Assert status code
        assert_status_code_is_200(response)

        # Parse and assert response JSON
        actual_response = parse_and_assert_response_json(response)

        # Load the expected response
        expected_response = load_expected_json("./data/json/respond_user_created.json")
        assert actual_response == expected_response, "The API response does not match the expected JSON file"

        # Attach responses to Allure
        attach_responses_to_allure(actual_response, expected_response)


@allure.parent_suite("API tests")
@allure.suite("User")
@allure.tag("API Test")
@allure.title("Test Case 2: GET user account detail by email")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    API URL: https://automationexercise.com/api/getUserDetailByEmail
    Request Method: GET
    Request Parameters: email
    Verify: 
    1. Response Code: 200
    2. Response JSON: User Detail matches expected data""")
@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_user_details():
    email = "max.mustermann@example.com"
    api_url = f"https://automationexercise.com/api/getUserDetailByEmail?email={email}"
    LOGGER.info(f"Testing API: {api_url}")

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

        # Assert status code
        assert_status_code_is_200(response)

        # Parse and assert response JSON
        actual_response = parse_and_assert_response_json(response)

        # Load the expected response
        expected_response = load_expected_json("./data/json/respond_user_detail.json")
        # Exclude dynamic field
        actual_response['user'].pop('id', None)
        assert actual_response == expected_response, "The API response does not match the expected JSON file"

        # Attach responses to Allure
        attach_responses_to_allure(actual_response, expected_response)


@allure.parent_suite("API tests")
@allure.suite("User")
@allure.tag("API Test")
@allure.title("Test Case 3: DELETE user account")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
    API URL: https://automationexercise.com/api/deleteAccount
    Request Method: DELETE
    Request Parameters: email, password
    Verify: 
    1. Response Code: 200
    2. Response Body: Account deleted!""")
@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_delete_user_account():
    request_data = {
        "email": "max.mustermann@example.com",
        "password": "password",
    }
    api_url = "https://automationexercise.com/api/deleteAccount"
    LOGGER.info(f"Testing API: {api_url}")

    async with httpx.AsyncClient() as client:
        response = await client.request(method="DELETE", url=api_url, data=request_data)

        # Assert status code
        assert_status_code_is_200(response)

        # Parse and assert response JSON
        actual_response = parse_and_assert_response_json(response)

        # Load the expected response
        expected_response = load_expected_json("./data/json/respond_user_deleted.json")
        assert actual_response == expected_response, "The API response does not match the expected JSON file"

        # Attach responses to Allure
        attach_responses_to_allure(actual_response, expected_response)


@allure.parent_suite("API tests")
@allure.suite("Products")
@allure.tag("API Test")
@allure.title("Test Case 1: GET All Products List")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    API URL: https://automationexercise.com/api/productsList
    Request Method: GET
    Verify: 
    1. Response Code: 200
    2. Response JSON: All products list matches expected data""")
@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_product_list():
    api_url = "https://automationexercise.com/api/productsList"
    LOGGER.info(f"Testing API: {api_url}")

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

        # Assert status code
        assert_status_code_is_200(response)

        # Parse and assert response JSON
        actual_response = parse_and_assert_response_json(response)

        # Load the expected response
        expected_response = load_expected_json("./data/json/respond_products_list.json")
        assert actual_response == expected_response, "The API response does not match the expected JSON file"

        # Attach responses to Allure
        attach_responses_to_allure(actual_response, expected_response)


@allure.parent_suite("API tests")
@allure.suite("Products")
@allure.tag("API Test")
@allure.title("Test Case 2: GET All Brands List")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
    API URL: https://automationexercise.com/api/brandsList
    Request Method: GET
    Verify: 
    1. Response Code: 200
    2. Response JSON: All brands list matches expected data""")
@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_get_all_brands_list():
    api_url = "https://automationexercise.com/api/brandsList"
    LOGGER.info(f"Testing API: {api_url}")

    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)

        # Assert status code
        assert_status_code_is_200(response)

        # Parse and assert response JSON
        actual_response = parse_and_assert_response_json(response)

        # Load the expected response
        expected_response = load_expected_json("./data/json/respond_brands_list.json")
        assert actual_response == expected_response, "The API response does not match the expected JSON file"

        # Attach responses to Allure
        attach_responses_to_allure(actual_response, expected_response)
