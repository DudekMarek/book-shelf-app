from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from app.main import app
from app.models.category_model import CategoryModel

client = TestClient(app)


def test_get_categories(mock_db_session):
    mock_db_session.query().all.return_value = [{"id": 1, "name": "sci-fi"}]

    response = client.get("/categories/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "sci-fi"


def test_get_category(mock_db_session):
    mock_db_session.query().filter().first.return_value = {"id": 1, "name": "sci-fi"}

    response = client.get("/categories/1")

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "sci-fi"


def test_create_category(mock_db_session):
    response = client.post("/categories/", json={"name": "sci-fi"})

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "sci-fi"

    mock_db_session.add.assert_called()
    mock_db_session.refresh.assert_called()
    mock_db_session.commit.assert_called()


def test_update_category(mock_db_session):
    mock_category = CategoryModel(id=1, name="sci-fi")
    mock_db_session.query().filter().first.return_value = mock_category

    response = client.put("/categories/1", json={"name": "fantasy"})

    assert response.status_code == 200

    data = response.json()
    print("Response Text:", data)
    assert data["name"] == "fantasy"

    assert mock_db_session.commit.called
    assert mock_db_session.refresh.called
