import sys
import json
from client import QuaternionSO3

def handle_call(name, arguments):
    if name == "slerp":
        q1 = QuaternionSO3(*arguments["q1"])
        q2 = QuaternionSO3(*arguments["q2"])
        t = arguments.get("t", 0.5)
        res = q1.slerp(q2, t)
        return {"w": res.w, "x": res.x, "y": res.y, "z": res.z}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
