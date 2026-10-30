
import pytest
from app import StudentManagement


@pytest.fixture
def system():
    return StudentManagement()


def test_add_student(system):
    result = system.add_student(
        "101", "Rahul", 20, "Python"
    )
    assert result == "Student added successfully"


def test_view_students(system):
    system.add_student("101", "Rahul", 20, "Python")
    assert len(system.view_students()) == 1


def test_search_student(system):
    system.add_student("101", "Rahul", 20, "Python")
    student = system.search_student("101")
    assert student["name"] == "Rahul"


def test_delete_student(system):
    system.add_student("101", "Rahul", 20, "Python")
    assert system.delete_student("101") is True
    assert system.search_student("101") is None


def test_duplicate_student_id(system):
    system.add_student("101", "Rahul", 20, "Python")

    with pytest.raises(ValueError):
        system.add_student("101", "Arun", 21, "Java")


def test_invalid_age(system):
    with pytest.raises(ValueError):
        system.add_student("102", "Ravi", -5, "Java")
