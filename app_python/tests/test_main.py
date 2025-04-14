def test_main(mocker):
    mocker.patch(
            "fastapi.applications.FastAPI"
    )
    mocker.patch(
            "uvicorn.main.run"
    )
