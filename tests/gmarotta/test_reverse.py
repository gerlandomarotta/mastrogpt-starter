import sys 
sys.path.append("packages/gmarotta/reverse")
import reverse

def test_reverse():
    args = {}
    res = reverse.reverse(args)
    assert res["output"] == "Plese provide some input"

    args = {"input": "hello"}
    res = reverse.reverse(args)
    assert res["output"] == "olleh"
    
    args = {"input": "ciao"}
    res = reverse.reverse(args)
    assert res.get("output") == "oaic"