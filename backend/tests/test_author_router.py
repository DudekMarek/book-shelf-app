from fastapi.testclient import TestClient

from app.main import app
from app.models import author_model

client = TestClient(app=app)


# def test_create_author(mock_db_session):
#     response = client.post(
#         "/authors/",
#         json={"name": "J.K. Rowling", "birth_year": 1965, "nationality": "British"},
#     )

#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == "J.K. Rowling"
#     assert data["birth_year"] == 1965
#     assert data["nationality"] == "British"

#     assert mock_db_session.add.called
#     assert mock_db_session.refresh.called
#     assert mock_db_session.commit.called
