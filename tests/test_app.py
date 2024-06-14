import pytest
from factory import create_app

@pytest.fixture
def client():
    app = create_app()
    
    with app.test_client() as client:
        yield client
        
    del app
        
def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200 
    assert response.get_json() == []
    
def test_add_task(client):
    response = client.post("/tasks", json={"task": "Test task"})
    assert response.status_code == 201
    assert response.get_json() == {"msg": "Task added"}
    
def test_add_task_without_task_data(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
    assert response.get_json() == {"msg": "No task provided"}
    
def test_delete_task(client):
    client.post("/tasks", json={"task": "Test task"})
    response = client.delete("/tasks/0")
    assert response.status_code == 200
    assert response.get_json() == {"msg": "Task deleted"}
    
    
def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/0")
    assert response.status_code == 404
    assert response.get_json() == {"msg": "Task not found"}
    
def test_complete_task(client):
    client.post("/tasks", json={"task": "Test task"})
    response = client.patch("/tasks/0/complete")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Task marked as complete!"}
    
def test_complete_nonexistent_task(client):
    t = client.get("/tasks")
    response = client.patch("/tasks/0/complete")
    
    print(t.get_json())
    
    assert response.status_code == 404
    assert response.get_json() == {"message": "Task not found!"}