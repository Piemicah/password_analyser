import { useState } from "react";
import "./App.css";
import axios from "axios";
import { Button, TextField } from "@mui/material";

function App() {
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState<string | null>(null);

  const passwordChecker = async () => {
    if (password === "") {
      setMessage("Password can not be empty");
      return;
    }

    await axios
      .post("http://127.0.0.1:8000/api/password/", { password })
      .then((res) => {
        setMessage(res.data.type);
      })
      .catch((err) => {
        console.log(err.message);
      });
  };

  return (
    <div className="flex flex-col items-center">
      <h1 className="text-4xl font-bold">
        WELCOME TO PASSWORD STRENGTH ANALYSER
      </h1>
      <div className="flex flex-col items-center gap-6 mt-12">
        <div className="flex">
          <TextField
            label="Enter Password"
            type="text"
            value={password}
            onChange={(e) => {
              setMessage(null);
              setPassword(e.target.value);
            }}
          />
        </div>
        <Button
          variant="contained"
          color="success"
          onClick={passwordChecker}
          className="w-28"
        >
          Check
        </Button>
      </div>
      {message && <h2 className="text-3xl">{message} password</h2>}
    </div>
  );
}

export default App;
