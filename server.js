const express = require("express");
const fs = require("fs");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

// Middleware to parse JSON and serve static files
app.use(bodyParser.json({ limit: "10mb" }));
app.use(express.static(path.join(__dirname)));

app.post("/save-json/:state", (req, res) => {
  const state = req.params.state;
  const data = req.body;

  const outputDir = path.join(__dirname, "State JSON Files");
  const outputPath = path.join(outputDir, `${state}.json`);

  // Ensure the output folder exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir);
  }

  fs.writeFile(outputPath, JSON.stringify(data, null, 2), (err) => {
    if (err) {
      console.error("Error writing JSON:", err);
      return res.status(500).send("Failed to save JSON file.");
    }
    res.send("Saved successfully.");
  });
});

app.listen(PORT, () => {
  console.log(`✅ Server running at http://localhost:${PORT}`);
});
