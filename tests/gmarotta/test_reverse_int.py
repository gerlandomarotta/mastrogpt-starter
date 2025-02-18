import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/gmarotta/reverse"
    res = req.get(url).json()
    assert res.get("output") == "Plese provide some input"

    res = req.post(url, json={"input": "hello"}).json()
    assert res.get("output") == "olleh"