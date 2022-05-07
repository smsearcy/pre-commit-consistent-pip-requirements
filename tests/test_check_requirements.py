from consistent_pip_requirements import check_requirements


def test_project_requirements(data_path):
    project_folder = data_path / "project"

    requirements_files = check_requirements._find_requirements_files(project_folder)

    assert len(requirements_files) == 2
    filenames = {path.name for path in requirements_files}
    expected = {"requirements.txt", "requirements-dev.txt"}
    assert filenames == expected


def test_folder_requirements(data_path):

    requirements_files = check_requirements._find_requirements_files(data_path)

    assert len(requirements_files) == 2
    filenames = {path.name for path in requirements_files}
    expected = {"dev.txt", "main.txt"}
    assert filenames == expected


def test_read_requirements(data_path):
    requirements_file = data_path / "project" / "requirements.txt"

    requirements = check_requirements._read_requirements(requirements_file)

    expected = {
        "attrs": "21.4.0",
        "certifi": "2021.10.8",
        "charset-normalizer": "2.0.12",
        "idna": "3.3",
        "requests": "2.27.1",
        "urllib3": "1.26.9",
    }
    assert requirements == expected


def test_consistent_requirements():
    requirements1 = {"foo": "1.0", "bar": "1.2", "baz": "1.1"}
    requirements2 = {
        "foo": "1.0",
        "bar": "1.2",
    }
    assert check_requirements._compare_requirements(requirements1, requirements2)


def test_inconsistent_requirements():
    requirements1 = {"foo": "1.0", "bar": "1.2", "baz": "1.1"}
    requirements2 = {
        "foo": "1.0",
        "bar": "1.2.1",
    }
    assert not check_requirements._compare_requirements(requirements1, requirements2)
